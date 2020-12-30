from color import WHITE

class Spot:

    SIZE = 20
    OFFSET = 50
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = self.col * self.SIZE + self.OFFSET
        self.y = self.row * self.SIZE + self.OFFSET
        self.color = WHITE
        self.isWall = False
        self.isDot = False
        self.isItem = False
        self.neighbours = list()
        self.isClosed = False

    