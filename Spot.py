from color import *
import pygame

class Spot:

    SIZE = 20
    OFFSET = 50

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = self.col * self.SIZE + self.OFFSET
        self.y = self.row * self.SIZE + self.OFFSET
        self.color = WHITE
        self.isWall = False
        self.isDot = False
        self.isItem = False
        self.neighbours = list()
        self.isClosed = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.SIZE, self.SIZE), 0)
    
    def get_pos(self):
        return self.x, self.y

    def get_dims(self):
        return self.row, self.col

    def make_dot(self):
        self.isDot = True
        self.color = SKIN

    def eat_dot(self):
        self.isDot = False
        self.color = WHITE

    def is_dot(self):
        return self.isDot

    def make_wall(self):
        self.isWall = True
        self.color = BLACK

    def is_wall(self):
        return self.isWall

    def make_path(self):
        self.isWall = False
        self.color = WHITE

    def make_player(self):
        self.isItem = True
        self.color = YELLOW

    def is_closed(self):
        return self.isClosed

    def close(self):
        self.isClosed = True

    def make_blinky(self):
        self.isItem = True
        self.color = pygame.color.THECOLORS['red2']

    def make_pinky(self):
        self.isItem = True
        self.color = pygame.color.THECOLORS['pink2']

    def make_inky(self):
        self.isItem = True
        self.color = pygame.color.THECOLORS['cyan2']

    def make_clyde(self):
        self.isItem = True
        self.color = pygame.color.THECOLORS['yellow2']

    def remove_item(self):
        self.isItem = False
        self.color = WHITE

    def is_empty(self):
        return not (self.isItem or self.isWall)

    def update_neighbors(self):
        pass
    
