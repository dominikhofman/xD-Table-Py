import colorsys
from display import Color
import math

class SinRainbow(object):
    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor

    def step(self, dt):
        self.hue += self.dhue * dt
        self.phase += self.dphase * dt

    def get_y(self, x):
        part = (math.sin(x / 2.0 + self.phase) + 1.0) / 2.0
        part = part * 8 + 1
        return int(part)

    def render(self, display):
        display.fill(Color())
        shift = 0
        for x in range(display.width):
            y = self.get_y(x)
            hue = (self.hue + shift) % 1
            if self.bor.get(x, y):
                hue += 0.5
            c = Color(
                *colorsys.hsv_to_rgb(hue, self.sat, self.val))
            for dy in range(self.sinewidth):
                display.set(x, y + dy, c)
                display.set(x, y - dy, c)
            shift += self.dshift

    def set_defaults(self):
        self.hue = 0
        self.dhue = 0.3
        self.ddhue = 0.1
        self.dshift = 0.05
        self.phase = 0.0
        self.dphase = 4
        self.sat = 1
        self.dsat = 0.1
        self.val = 255
        self.dval = 3
        self.sinewidth = 2

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
