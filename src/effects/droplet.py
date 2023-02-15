import colorsys
from utils.display import Color
from random import random
import math


class Droplet(object):
    def dist_to_circle(self, x, y):
        dist_from_cent = math.hypot(self.cx - x, self.cy -y)
        dist_from_circle = abs(dist_from_cent - self.cr)
        return dist_from_circle

    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor
        self.dt = 0
        self.cx = 4.5
        self.cy = 4.5
        self.cr = .0
        self.dr = 3
        self.cc = Color.blue()

    def step(self, dt):
        self.cr += dt * self.dr
        if self.cr > 9.0:
            self.cr = 0.0

    def render(self, display):
        #display.fill(Color.blue())
        for y in range(display.height):
            for x in range(display.width):
                dist = self.dist_to_circle(x, y)

                dist = 1.0 / (dist + 1.0)
                if dist > 1.0:
                    print (dist)
            #    print(dist)
                display.set(x, y, Color.blue().fade(dist))
            #    if self.bor.get(x, y) or random() < (self.random_rate * self.dt):
            #        display.set(x, y, Color(
            #            *colorsys.hsv_to_rgb(random(), self.sat, self.val)))

    def set_defaults(self):
        pass
