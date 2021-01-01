import pygame
from Body import Body
from typing import Tuple

class Player(Body):

    def __init__(self):
        
        super().__init__('player')

        self.IMAGECOUNT = 3
        self.COOLDOWN = 10
        self.row = 17
        self.col = 14

        # set x and y for player
        self.set_x_and_y()

        # Loads all the images
        self.load_images()
    
