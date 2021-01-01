from pygame import Surface
from Body import Body

class Blinky(Body):

    def __init__(self):

        super().__init__('blinky')
        self.IMAGECOUNT = 2
        self.COOLDOWN = 9
        self.row = 11
        self.col = 14

        self.set_x_and_y()
        self.load_images()