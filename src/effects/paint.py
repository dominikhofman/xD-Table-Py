import colorsys
from utils.display import Color
from random import random
import math


class Paint(object):
    def dist_to_circle(self, x, y):
        dist_from_cent = math.hypot(self.cx - x, self.cy -y)
        dist_from_circle = abs(dist_from_cent - self.cr)
        return dist_from_circle

    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor
        self.palette = [Color.white(), Color.red(), Color.green(), Color.blue(),
                       Color(255,255,0), Color(0,255,255), Color(255,0,255),
                       Color(255,121,0), Color.black()]
        self.current = Color.blue()

    def step(self, dt):
        for i in range(self.bor.width - 1):
            if self.bor.get(i, self.bor.height - 1):
                self.current = self.palette[i]

    def render(self, display):
        for i, c in enumerate(self.palette):
            display.set(i, display.height - 1, c)
        display.set( display.height - 1, display.height - 1, self.current)
        for y in range(display.height - 1):
            for x in range(display.width):
                if self.bor.get(x, y):
                    display.set(x, y, self.current)


    def set_defaults(self):
        pass
