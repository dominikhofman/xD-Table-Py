import colorsys
from display import Color
from random import random
import math

def vector_from_angle(angle, magnitude):
    return (math.cos(angle) * magnitude, math.sin(angle) * magnitude) # x, y

class Ray(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.respawn()

    def respawn(self):
        self.x = 5
        self.y = -1
        self.x, self.y = vector_from_angle(math.pi * random() * 2.0, 10)
        self.x += 4.5
        self.y += 4.5
        self.dx, self.dy = vector_from_angle(math.pi * random() * 2.0, 10)
        self.c = Color(*colorsys.hsv_to_rgb(random(), 1, 255))
        self.lifetime = 50 * random()

    def is_on_screen(self, dt):
        # left border
        if self.x + self.dx * dt < 0:
            return False

        # right border
        if self.x + self.dx * dt > self.ctx.width:
            return False

        # up border
        if self.y + self.dy * dt < 0:
            return False

        # down border
        if self.y + self.dy * dt > self.ctx.height:
            return False
        return True

    def step(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.lifetime -= 1
        if self.lifetime < 0:
            if not self.is_on_screen(dt):
                self.respawn()
        #self.handle_collisions_with_borders(dt)

    def render(self, display):
        display.safe_set(self.x, self.y, self.c.clone())

class Rays(object):
    def __init__(self, bor):
        self.bor = bor
        self.width = bor.width
        self.height = bor.height
        self.fade_rate = 2
        self.dt = 0
        self.rays = [Ray(self), Ray(self), Ray(self), Ray(self), Ray(self), Ray(self), Ray(self),Ray(self), Ray(self), Ray(self), Ray(self), Ray(self), Ray(self), Ray(self)]

    def step(self, dt):
        self.dt = dt
        for r in self.rays:
            r.step(dt)

    def render(self, display):
        fade_shiet = 1.0 - (self.fade_rate * self.dt) % 1
        display.fade(fade_shiet)
        for r in self.rays:
            r.render(display)
