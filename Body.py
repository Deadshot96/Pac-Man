from typing import Tuple
from pygame import Surface
from settings import GRID_SIZE, GRID_OFFSET
import pygame
import os
from color import YELLOW

class Body(object):

    COOLDOWN = 5
    IMAGECOUNT = 0
    asset_dir = os.path.join(os.getcwd(), 'assets')
 
    def __init__(self, name: str):

        self.name = name
        self.row = 0
        self.col = 0
        self.x = 0
        self.y = 0
        self.moveRow = 0
        self.moveCol = 0
        self.angle = 0
        self.vel = 0

        self.animation_count = 0
        self.cooldown_count = 0
        self.imgDims = (28, 28)
        self.image = None

        self.up = []
        self.down = []
        self.right = []
        self.left = []

        self.angleDict = {0: self.right, 90: self.up,\
            180: self.left, 270: self.down}

    def cooldown(self) -> None:
        if self.cooldown_count > self.COOLDOWN:
            self.cooldown_count = 0
        elif self.cooldown_count > 0:
            self.cooldown_count += 1

    def get_pos(self) -> Tuple:
        return self.row, self.col

    def get_center_pos(self) -> Tuple:
        offset = self.imgDims[0] // 2
        return self.x + offset, self.y + offset

    def set_x_and_y(self) -> None:
        self.x = self.col * GRID_SIZE + GRID_OFFSET + GRID_SIZE // 2
        self.y = self.row * GRID_SIZE + GRID_OFFSET + GRID_SIZE // 2


    def draw(self, win: Surface) -> None:
        if self.cooldown_count == 0:
            self.cooldown_count = 1
            self.animation_count += 1

            if self.animation_count == self.IMAGECOUNT:
                self.animation_count = 0

        self.image = self.angleDict[self.angle][self.animation_count]
        # pygame.draw.circle(win, YELLOW, (self.x, self.y), 5)
        rect = self.image.get_rect()
        rect.center = (self.x, self.y)
        win.blit(self.image, rect)
        self.cooldown()

    def load_images(self) -> None:
        img_folder_path = os.path.join(self.asset_dir, self.name)

        for filename in os.listdir(img_folder_path):
            pic = pygame.transform.scale(pygame.image.load(os.path.join(img_folder_path, filename)), self.imgDims)
            
            if filename.startswith('up'):
                self.up.append(pic)
            elif filename.startswith('down'):
                self.down.append(pic)
            elif filename.startswith('right'):
                self.right.append(pic)
            elif filename.startswith('left'):
                self.left.append(pic)

    def is_cool(self) -> bool:
        return self.cooldown_count == 0

    def get_next_pos(self) -> Tuple:    
        row = self.row + self.moveRow
        col = self.col + self.moveCol

        return row, col

    def change_pos(self, row: int, col: int):
        self.row = row
        self.col = col

        self.set_x_and_y()
        
