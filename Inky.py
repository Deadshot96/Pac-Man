from pygame import Surface
from Body import Body

class Inky(Body):

    def __init__(self):

        super().__init__('inky')
        self.IMAGECOUNT = 2
        self.COOLDOWN = 9
        self.row = 14
        self.col = 12
        
        self.imgDims = (26, 26)
        self.scatter_path = None

        self.set_x_and_y()
        self.load_images()

        self.mode = ['scatter', 'fright', 'courage', 'dead']
