from __future__ import division
import colorsys
from display import Color
from noise import pnoise3

class Plasma(object):
    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor

    def step(self, dt):
        # pass
        # self.z += self.dz * dt
        self.shift_x += self.dx * dt
        self.shift_y += self.dy * dt
        # self.hue_off += self.dhue * dt

    def render(self, display):
        for y in range(display.height):
            for x in range(display.width):
                hue = (pnoise3((x / self.x_zoom) + self.shift_x, (y / self.y_zoom) + self.shift_y, self.z / self.z_zoom) + 1.0) / 2.0 
                hue += self.hue_off

                if self.bor.get(x, y):
                    hue += 0.5
                c = Color.hsv(hue+0.3)
                display.set(x, y, c)
                

    def set_defaults(self):
        self.z = 0.0
        self.dz = 0
        # self.dz = .2
        self.shift_x = 0
        self.dx = 0.0
        self.shift_y = 0
        self.dy = 0.2
        self.x_zoom = 7.0
        self.y_zoom = 7.0
        self.z_zoom = 1.0
        self.hue_off = 0.0
        self.dhue = 0.1
        
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
