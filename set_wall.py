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
        pygame.display.update()


    def isValidPos(self, row, col):
        pass

    
    def run(self) -> None:
        
        self.grid_init()

        run = True
        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

            self.draw(self.win)

        pygame.font.quit()
        pygame.quit()


if __name__ == '__main__':
    X = Temp()
    X.run()