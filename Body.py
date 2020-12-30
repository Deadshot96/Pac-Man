from typing import Tuple
from pygame import Surface

class Body(object):

    COOLDOWN = 5
    IMAGECOUNT = 0

    def __init__(self, name: str):

        self.name = name
        self.x = 0
        self.y = 0
        self.moveX = 0
        self.moveY = 0
        self.angle = 0
        self.vel = 0

        self.animation_count = 0
        self.cooldown_count = 0
        self.imgDims = (32, 32)

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
        return self.x, self.y

    def get_center_pos(self) -> Tuple:
        offset = self.imgDims[0] // 2
        return self.x + offset, self.y + offset

    def draw(self, win: Surface) -> None:
        if self.cooldown_count == 0:
            self.cooldown_count = 1
            self.animation_count += 1

            if self.animation_count == self.IMAGECOUNT:
                self.animation_count = 0

        self.image = self.angleDict[self.angle][self.animation_count]
        win.blit(self.image, (self.x, self.y))
        self.cooldown()
