import colorsys
from utils.display import Color


class Rainbow(object):
    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor

    def step(self, dt):
        self.hue += self.dhue * dt

    def render(self, display):
        shift = 0
        for y in range(display.height):
            for x in range(display.width):
                hue = (self.hue + shift) % 1
                if self.bor.get(x, y):
                    hue += 0.5
                display.set(x, y, Color(
                    *colorsys.hsv_to_rgb(hue, self.sat, self.val)))
                shift += self.dshift

    def set_defaults(self):
        self.hue = 0
        self.dhue = 0.3
        self.ddhue = 0.1
        self.dshift = 0.005
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
            # incrase hue change speed
            self.dhue += self.ddhue

        if key == 'g':
            # decrase hue change speed
            self.dhue -= self.ddhue

        if key == 'r':
            # reset to default
            self.set_defaults()
