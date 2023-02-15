import colorsys
from utils.display import Color
from random import random


class XDColor(object):
    def __init__(self, color):
        self.dt = 0
        img = """
        1111111111
        0111010011
        1010110101
        1010110110
        1101110110
        1101110110
        1010110110
        1010110101
        0111010011
        1111111111
        """
        data = img.split('\n')[1:-1]
        result = []
        for l in data:
            line = []
            l = l.strip()
            for c in l:
                line.append(color.clone() if c == '1' else color.clone().fade(0.5))
            result.append(line)
        self.data = result

    def step(self, dt):
        self.dt = dt

    def render(self, display):
        for y in range(display.height):
            for x in range(display.width):
                display.set(x, y, self.data[y][x])

