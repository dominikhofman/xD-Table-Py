import colorsys
from utils.display import Color, Display

import effects.text.constants as constants
import time

class Text(object):
    def __init__(self, bor):
        k = list(constants.font.keys())
        k.sort()
        self.set_text(0, 0, ''.join(k))
        self.color = Color(0, 0, 255)
        self.speed = 15
        self.repeat = True
        self.bor = bor

    def step(self, dt):
        self.shift -= dt * self.speed
        self.check_done()

    def render(self, display):
        display.fill(Color(0, 0, 0))
        for x in xrange(display.width):
            n = x - self.x - int(self.shift) - 1
            if n < len(self.buf) and n >= 0:
                self.render_col(x, self.y, n, display)

    def set_text(self, x, y, text):
        self.text = text
        self.x, self.sx = x, x
        self.y, self.sy = y, y
        self.shift = 0
        self.prepare_buf(text)
        self.done = False

    def prepare_buf(self, text):
        self.buf = []
        for c in self.text[:-1]:
            self.buf += constants.font[c]
            self.buf += [[]]
        self.buf += constants.font[self.text[-1]]

    def check_done(self):
        self.done = -self.shift > len(self.buf) + self.x
        if self.done and self.repeat:
            self.set_text(self.sx, self.sy, self.text)

    def render_col(self, x, y, n, display):
        for i, v in enumerate(self.buf[n]):
            ny = y + i
            if ny < 0 or ny > display.height:
                continue
            if v:
                display.set(x, y + i, self.color)

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


if __name__ == "__main__":
    s = Text()
    d = Display(10, 10)
    s.set_text(10, 1, "TEST")
    while not s.done:
        s.step(0.5)
        s.render(d)
        d.print_ascii()
        time.sleep(0.1)
