import pygame
from Body import Body
from typing import Tuple

class Player(Body):

    def __init__(self):
        
        super().__init__('player')

        self.IMAGECOUNT = 3
        self.COOLDOWN = 7
        self.row = 17
        self.col = 14

        # set x and y for player
        self.set_x_and_y()

        # Loads all the images
        self.load_images()
    
    def turn_up(self) -> None:
        self.moveRow = -1
        self.moveCol = 0
        self.angle = 90

    def turn_down(self) -> None:
        self.moveRow = 1
        self.moveCol = 0
        self.angle = 270

    def turn_right(self) -> None:
        self.moveRow = 0
        self.moveCol = 1
        self.angle = 0

    def turn_left(self) -> None:
        self.moveRow = 0
        self.moveCol = -1
        self.angle = 180

    def get_next_pos(self) -> Tuple:    
        row = self.row + self.moveRow
        col = self.col + self.moveCol

        return row, col

    def change_pos(self, row: int, col: int):
        self.row = row
        self.col = col

        self.set_x_and_y()