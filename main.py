import pygame
import os
import shelve
import time
import random
import math
import copy
from queue import PriorityQueue
import settings
from color import BLACK
from Grid import Grid
from Dot import Dot
class Game(object):

    asset_dir = os.path.join(os.getcwd(), 'assets')
    BG = pygame.image.load(os.path.join(asset_dir, 'colormap.png'))
    MOVEMAP = pygame.image.load(os.path.join(asset_dir, 'movemap.png'))
    DOTMAP = pygame.image.load(os.path.join(asset_dir, 'dotmap.png'))
    DOT = pygame.image.load(os.path.join(asset_dir, 'dot.png'))
    
    def __init__(self):

        self.rows = settings.GRID_ROWS
        self.cols = settings.GRID_COLS
        self.width = settings.WIDTH
        self.height = settings.HEIGHT
        self.size = settings.GRID_SIZE
        self.offset = settings.GRID_OFFSET
        self.fps = settings.FPS
        self.grid = None
        self.dots = None
        self.player = None
        self.clock = None
        self.win = None
        self.showWall = False
        
        
    def game_init(self) -> None:
        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pac-Man Developer")

        self.grid = Grid()
        self.dot_init()
        self.clock = pygame.time.Clock()
        
        self.win.fill(BLACK)
        pygame.display.update()

    def dot_init(self) -> None:
        self.dots = list()
        dot_len = settings.DOT_LEN
        size = settings.DOT_SIZE
        offset = settings.DOT_OFFSET

        for row in range(dot_len):
            self.dots.append(list())
            for col in range(dot_len):
                x = col * size + offset - self.offset
                y = row * size + offset - self.offset

                if self.is_valid_dot_pos(x, y):
                    dot = Dot(row, col, self.DOT)
                    self.dots[row].append(dot)
                    self.grid.make_dot(row + 1, col + 1)


    def is_valid_dot_pos(self, x: int, y: int) -> bool:
        return self.DOTMAP.get_at((x, y)) == (0, 0, 0)


    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.BG, (self.offset, self.offset))

        if self.showWall:
            self.grid.draw_dots(self.win)
        self.draw_dots(win)
        pygame.display.update()


    def draw_dots(self, win: pygame.Surface) -> None:
        for row in self.dots:
            for dot in row:
                if not dot.is_eaten():
                    dot.draw(win)

    def run(self) -> None:

        self.game_init()
        
        run = True
        while run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.grid.get_grid_dims(pos)
                    print(row, col, sep='\t')

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_SPACE]:
                        self.showWall = not self.showWall

            self.draw(self.win)

        pygame.font.quit()
        pygame.quit()



if __name__ == '__main__':
    X = Game()
    X.run()


