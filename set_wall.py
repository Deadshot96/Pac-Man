import shelve
import pygame
import math
from Grid import Grid
from settings import WIDTH, HEIGHT, OFFSET, FPS
from color import BLACK


class Temp(object):
    
    def __init__(self):

        self.width = WIDTH
        self.height = HEIGHT
        self.offset = OFFSET
        self.win = None
        self.clock = None
        self.grid = None

    def grid_init(self):

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pac-Man")

        self.clock = pygame.time.Clock()
        self.grid = Grid()

        self.win.fill(BLACK)
        pygame.display.update()

