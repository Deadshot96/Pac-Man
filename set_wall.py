import shelve
import pygame
import math
import os
from Grid import Grid
from settings import WIDTH, HEIGHT, OFFSET, FPS
from color import BLACK


class Temp(object):
    
    asset_dir = os.path.join(os.getcwd(), 'assets')
    BG = pygame.image.load(os.path.join(asset_dir, 'colormap.png'))
    MOVEMAP = pygame.image.load(os.path.join(asset_dir, 'movemap.png'))
    DOTMAP = pygame.image.load(os.path.join(asset_dir, 'dotmap.png'))
    DOT = pygame.image.load(os.path.join(asset_dir, 'dot.png'))
    

    def __init__(self):

        self.width = WIDTH
        self.height = HEIGHT
        self.offset = OFFSET
        self.win = None
        self.clock = None
        self.grid = None

    def grid_init(self) -> None:

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pac-Man")

        self.clock = pygame.time.Clock()
        self.grid = Grid()

        self.win.fill(BLACK)
        pygame.display.update()


    def draw(self, win: pygame.Surface) -> None:

        movemap = self.MOVEMAP.convert()
        movemap.set_alpha(128)

        win.blit(self.BG, (self.offset, self.offset))
        win.blit(movemap, (self.offset, self.offset))

        

        self.grid.draw_lines(win)
        pygame.display.update()



    
    def run(self) -> None:
        
        self.grid_init()
        wall = list()
        run = True
        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                pressed = pygame.mouse.get_pressed()
                
                if pressed[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = self.grid.get_grid_dims(pos)
                    # print(row, col, sep='\t')

                    if self.grid.is_valid_pos

                if pressed[2]:
                    pos = pygame.mouse.get_pos()
                    row, col = self.grid.get_grid_dims(pos)

                    if self.grid.is_valid_pos(row, col):
                        pass


                    

            self.draw(self.win)

        pygame.font.quit()
        pygame.quit()


if __name__ == '__main__':
    X = Temp()
    X.run()