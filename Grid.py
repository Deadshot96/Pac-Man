import pygame
import os
import settings
import shelve
from Spot import Spot
from color import YELLOW
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

    def draw_lines(self, win: pygame.surface) -> None:
        for x in range(GRID_OFFSET, GRID_OFFSET + GRID_COLS * GRID_SIZE + 5, GRID_SIZE):
            pygame.draw.line(win, YELLOW, (x, GRID_OFFSET), (x, 630), 1)

        for y in range(GRID_OFFSET, GRID_OFFSET + GRID_ROWS * GRID_SIZE + 5, GRID_SIZE):
            pygame.draw.line(win, YELLOW, (GRID_OFFSET, y), (650, y), 1)


    def draw_grid(self, win: pygame.surface) -> None:
        for row in self.grid:
            for spot in row:
                spot.draw(win)

    def get_spot(self, row: int, col: int) -> Spot:
        return self.grid[row][col]