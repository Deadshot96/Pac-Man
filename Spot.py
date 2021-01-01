from color import *
import pygame
from settings import GRID_SIZE, GRID_OFFSET

class Spot:

    SIZE = GRID_SIZE
    OFFSET = GRID_OFFSET

    def __init__(self, row: int, col: int):
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

    def draw(self, win: pygame.Surface):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.SIZE, self.SIZE), 0)
    
    def get_pos(self) -> None:
        return self.x, self.y

    def get_dims(self) -> None:
        return self.row, self.col

    def make_dot(self) -> None:
        self.isDot = True
        self.color = SKIN

    def eat_dot(self) -> None:
        self.isDot = False
        self.color = WHITE

    def is_dot(self) -> bool:
        return self.isDot

    def make_wall(self) -> None:
        self.isWall = True
        self.color = CORAL

    def is_wall(self) -> bool:
        return self.isWall

    def is_path(self) -> bool:
        return not self.isWall

    def make_path(self) -> None:
        self.isWall = False
        self.color = WHITE

    def make_player(self) -> None:
        self.isItem = True
        self.color = YELLOW

    def is_closed(self) -> bool:
        return self.isClosed

    def close(self) -> bool:
        self.isClosed = True

    def open(self) -> None:
        self.isClosed = False

    def make_blinky(self) -> None:
        self.isItem = True
        self.color = pygame.color.THECOLORS['red2']

    def make_pinky(self) -> None:
        self.isItem = True
        self.color = pygame.color.THECOLORS['pink2']

    def make_inky(self) -> None:
        self.isItem = True
        self.color = pygame.color.THECOLORS['cyan2']

    def make_clyde(self) -> None:
        self.isItem = True
        self.color = pygame.color.THECOLORS['yellow2']

    def remove_item(self) -> None:
        self.isItem = False
        self.color = WHITE

    def is_empty(self) -> bool:
        return not (self.isItem or self.isWall)

    def update_neighbors(self) -> None:
        pass

