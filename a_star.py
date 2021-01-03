import pygame
from settings import GRID_ROWS, GRID_COLS
from queue import PriorityQueue
from Grid import Grid
from Body import Body
from Player import Player

def a_star(grid: Grid, ghost: Body, player: Player):
    

    def h_dist(pos1, pos2):
        row1, col1 = pos1
        row2, col2 = pos2

        return abs(row1 - row2) + abs(col1 - col2)

    start = ghost.get_pos()

    # Update neighbours - somehow do it quickly enough

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    open_set_hash = set()
    open_set_hash.add(start)
    came_from = {}

    
