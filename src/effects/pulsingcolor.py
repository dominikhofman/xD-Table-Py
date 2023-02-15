import colorsys
from utils.display import Color
from copy import copy
from math import sin

class PulsingColor(object):
    def __init__(self, color):
        self.base_color = color
        self.phase = 0
        self.dphase = 5

    def step(self, dt):
        self.phase += self.dphase * dt

    def render(self, display):
        c = copy(self.base_color)
        c.fade((sin(self.phase) + 1.0) / 2.0)
        display.fill(c)

    def on_press(self, key):
        pass
