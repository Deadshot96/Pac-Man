import pygame
import os
import settings
import shelve
from Spot import Spot
from settings import GRID_COLS, GRID_ROWS, GRID_SIZE, GRID_OFFSET

class Grid(object):

    asset_dir = os.path.join(os.getcwd(), 'assets_pac_man')

    def __init__(self):
        super().__init__()
        self.grid = None
        self.ghosts = None
        self.player = None
        self.wall = list()
        self.dots = list()
        
        # Making grid
        self.grid_init()


    def grid_init(self):
        self.grid = list()

        for row in self.range(GRID_ROWS):
            self.grid.append(list())

            for col in self.range(GRID_COLS):
                spot = Spot(row, col)
                self.grid[row].append(spot)

        
