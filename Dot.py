from settings import DOT_SIZE, DOT_OFFSET, DOT_LEN
from pygame import Surface
class Dot(object):

    def __init__(self, row: int, col: int, img: Surface):
        self.row = row
        self.col = col
        self.dot = img
        self.x = self.col * DOT_SIZE + DOT_OFFSET
        self.y = self.row * DOT_SIZE + DOT_OFFSET
        self.isEaten = False

    def draw(self, win: Surface) -> None:
        win.blit(self.dot, (self.x, self.y))

    def eat(self) -> None:
        self.isEaten = True

    def is_eaten(self) -> bool:
        return self.isEaten

    
