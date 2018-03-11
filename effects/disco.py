import colorsys
from display import Color
from copy import copy
from math import sin, pi

class Disco(object):
    def __init__(self):
        self.phase = 0
        self.dphase = 5.0
        self.colors = [Color(255,182,193),  Color(127, 255, 212),  Color(240, 230, 140),  Color(165, 214, 167),  Color(211, 211, 211),  Color(129, 199, 132)]

    def step(self, dt):
        self.phase += self.dphase * dt

    def render(self, display):
        c = copy(self.colors[ int(self.phase % len(self.colors))])
        c.fade((sin(self.phase * pi * 2.0 ) + 1.0) / 2.0)
        display.fill(c)

    def on_press(self, key):
        pass
