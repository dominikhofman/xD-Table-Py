import colorsys
import copy
from display import Color
import math
from tmp import dist_to_sine

class SinRainbow2(object):
    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor

    def step(self, dt):
        self.hue += self.dhue * dt
        self.phase += self.dphase * dt

    def get_y(self, x):
        y = (self.const + self.amp * math.sin(self.freq * x  + self.phase)) 
        return int(round(y))

    def render(self, display):
        display.fill(Color())
        shift = 0
        for x in range(display.width):
            hue = (self.hue + shift) % 1
            #if self.bor.get(x, y):
            #    hue += 0.5
            c = Color(
                *colorsys.hsv_to_rgb(hue, self.sat, self.val))

            for y in range(display.height):

                dist = dist_to_sine(x, y, self.const, self.amp, self.freq, self.phase) 
                dist = 1.0 / (1.0 + dist) 

                cp = copy.copy(c)
                cp.fade(dist)

                display.set(x, y, cp)

            shift += self.dshift


    def set_defaults(self):
        self.hue = 0
        self.dhue = 0.3
        self.ddhue = 0.1
        self.dshift = 0.05
        self.sat = 1
        self.dsat = 0.1
        self.val = 255
        self.dval = 3

        # y = const + amp * sin(freq * x + phase)

        self.phase = 0.0 # d
        self.dphase = 4

        self.freq = 0.5 # c
        self.const = 4.5 # a
        self.amp = 3.5 # b

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
