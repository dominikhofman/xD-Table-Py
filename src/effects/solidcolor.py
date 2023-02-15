import colorsys
from utils.display import Color


class SolidColor(object):
    def __init__(self, color):
        self.color = color

    def step(self, dt):
        pass

    def render(self, display):
        display.fill(self.color)

    def on_press(self, key):
        pass
