import colorsys
from display import Color


class Red(object):
    def __init__(self):
        pass

    def step(self, dt):
        pass

    def render(self, display):
        for y in range(display.height):
            for x in range(display.width):
                display.set(x, y, Color(255, 0, 0))

    def on_press(self, key):
        pass
