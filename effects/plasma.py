from __future__ import division
import colorsys
from display import Color
from noise import pnoise3

class Plasma(object):
    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor

    def step(self, dt):
        self.z += self.dz * dt

    def render(self, display):
        for y in range(display.height):
            for x in range(display.width):
                hue = (pnoise3(x / self.x_zoom, y / self.y_zoom, self.z / self.z_zoom) + 1.0) / 2.0
                if self.bor.get(x, y):
                    hue += 0.5
                c = Color.hsv(hue)
                display.set(x, y, c)

    def set_defaults(self):
        self.z = 0.0
        self.dz = .1
        self.x_zoom = 10.0
        self.y_zoom = 10.0
        self.z_zoom = 1.0


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
