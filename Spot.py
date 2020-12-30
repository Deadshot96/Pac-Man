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
