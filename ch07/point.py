import random
from pygame import Rect

class Point: 
    def __init__(self, x=0, y=0, size = 20):
        self.on = True
        self.rect = Rect(abs(x), abs(y), size, size)
        self.xcoor = abs(x)
        self.ycoor = abs(y)
        self.color = self.random_color()

    def random_color(self): 
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))