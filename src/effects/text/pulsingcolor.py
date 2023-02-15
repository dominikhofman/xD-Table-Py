import colorsys
from display import Color
from copy import copy
from math import sin

class PulsingColor(object):
    def __init__(self, color):
        self.base_color = color
        self.phase = 0
        self.dphase = 10

    def step(self, dt):
        self.phase += self.dphase * dt
        print(self.phase)

    def render(self, display):
        c = copy(self.base_color)
        c.fade(sin(self.phase))
        display.fill(c)

    def on_press(self, key):
        pass
