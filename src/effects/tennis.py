from __future__ import division
import colorsys
from random import random, randint
from utils.display import Color


class Ball(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.c = Color.white()
        self.dt = 0
        self.speed = 1
        self.reset()

    def handle_collisions_with_borders(self, dt):
        # left border
        if self.x + self.dx * dt < 0:
            self.x = 0
            self.dx *= -1

        # right border
        if self.x + self.dx * dt > self.ctx.width:
            self.x = self.ctx.width - 1
            self.dx *= -1

    def handle_collisions_paddles(self, display):
        c1 = display.safe_get(self.x + self.dx * self.dt, self.y)
        if c1 != Color.black() and c1 != Color.white():
            self.dx *= -1
        c2 = display.safe_get(self.x, self.y + self.dy * self.dt)
        if c2 != Color.black() and c2 != Color.white():
            self.dy *= -1

    def check_win_cond(self):
        if int(self.y + self.dy * self.dt) == self.ctx.height:
            return 1
        if int(self.y + self.dy * self.dt) == -1:
            return 2
        return 0

    def update(self, dt, bor):
        self.handle_collisions_with_borders(dt)
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.dt = dt
        self.dy += self.speed * dt if self.dy > 0 else - self.speed * dt
        self.dx += self.speed * dt if self.dx > 0 else - self.speed * dt

    def render(self, display):
        display.set(int(self.x), int(self.y), self.c)

    def reset(self):
        self.x = self.ctx.width / 2
        self.y = self.ctx.height / 2
        self.dx = 2
        self.dy = 3


class Paddle(object):
    def __init__(self, ctx, y, c):
        self.ctx = ctx
        self.x = ctx.width / 2
        self.y = y
        self.c = c

    @staticmethod
    def avg(l):
        return sum(l) / len(l)

    def update(self, dt, bor):
        l = [i for i, val in enumerate(bor.row(self.y)) if val]
        if len(l) > 0:
            self.x = int(Paddle.avg(l))

    def render(self, display):
        display.safe_set(self.x + 1, self.y, self.c)
        display.safe_set(self.x, self.y, self.c)
        display.safe_set(self.x - 1, self.y, self.c)

class Tennis(object):
    def __init__(self, bor):
        self.set_defaults()
        self.bor = bor
        self.width = bor.width
        self.height = bor.height
        self.ball = Ball(self)
        self.paddle1 = Paddle(self, 0, Color.red())
        self.paddle2 = Paddle(self, bor.height - 1, Color.blue())
        self.win_animation = False
        self.factor = 1.0
        self.dfactor = 0.9

    def step(self, dt):
        if self.win_animation:
            self.factor *= self.dfactor
            if self.factor < 0.05:
                self.win_animation = False
            return

        self.ball.update(dt, self.bor)
        self.paddle1.x = self.ball.x
        self.paddle2.x = self.ball.x
        self.paddle1.update(dt, self.bor)
        self.paddle2.update(dt, self.bor)
        win_cond = self.ball.check_win_cond()
        if win_cond:
            self.ball.reset()
            self.win_animation = True
            self.factor = 1.0
            self.winner =  win_cond

    def render(self, display):
        if self.win_animation:
            if self.winner == 1:
                c = self.paddle1.c.clone()
                display.fill(c.fade(self.factor))

            if self.winner == 2:
                c = self.paddle2.c.clone()
                display.fill(c.fade(self.factor))
            return

        display.fill(Color(0, 0, 0))
        self.ball.render(display)
        self.paddle1.render(display)
        self.paddle2.render(display)
        self.ball.handle_collisions_paddles(display)


        # for b in self.balls:
        #    display.set(int(b.x), int(b.y), Color(255, 255, 255))

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
