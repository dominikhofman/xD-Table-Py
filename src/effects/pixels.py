import colorsys
from utils.display import Color
from random import random


class Pixels(object):
    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor
        self.dt = 0

    def step(self, dt):
        self.dt = dt

    def render(self, display):
        fade_shiet = 1.0 - (self.fade_rate * self.dt) % 1
        display.fade(fade_shiet)
        for y in range(display.height):
            for x in range(display.width):
                if self.bor.get(x, y) or random() < (self.random_rate * self.dt):
                    display.set(x, y, Color(
                        *colorsys.hsv_to_rgb(random(), self.sat, self.val)))

    def set_defaults(self):
        self.random_rate = 0.5
        self.drandom_rate = 0.1
        self.fade_rate = 2
        self.dfade_rate = 0.2
        self.sat = 1
        self.dsat = 0.1
        self.val = 255
        self.dval = 3

    def on_press(self, key):
        if key == 'w':
            # incrase value
            self.val += self.dval
            if self.val > 255:
                self.val = 255

        if key == 's':
            # decrase value
            self.val -= self.dval
            if self.val < 0:
                self.val = 0

        if key == 'd':
            # incrase saturation
            self.sat += self.dsat
            if self.sat > 1:
                self.sat = 1

        if key == 'a':
            # decrase saturation
            self.sat -= self.dsat
            if self.sat < 0:
                self.sat = 0

        if key == 'f':
            # incrase random_rate change speed
            self.random_rate += self.drandom_rate

        if key == 'g':
            # decrase random_rate change speed
            self.random_rate -= self.drandom_rate

        if key == 'v':
            # incrase fade_rate change speed
            self.fade_rate += self.dfade_rate

        if key == 'b':
            # decrase fade_rate change speed
            self.fade_rate -= self.dfade_rate
        if key == 'r':
            # reset to default
            self.set_defaults()
