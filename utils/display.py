from itertools import chain
from copy import copy

class Color(object):
    def __init__(self, r=0, g=0, b=0):
        self.r, self.g, self.b = r, g, b

    def __getitem__(self, n):
        if n == 0: return self.r
        if n == 1: return self.g
        if n == 2: return self.b

    def get_brightness(self):
        return (self.r + self.g + self.b) / 3.0

    def fade(self, factor):
        self.r *= factor
        self.g *= factor
        self.b *= factor

    def safe_fade(self, factor):
        self.r *= factor
        self.g *= factor
        self.b *= factor
        if self.r > 255: self.r = 255
        if self.g > 255: self.g = 255
        if self.b > 255: self.b = 255
        if self.r < 0: self.r = 0
        if self.g < 0: self.g = 0
        if self.b < 0: self.b = 0

class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [ 0 for i in range(width * height) ]

    def set(self, x, y, c):
        self.data[y * self.width + x] = c

    def get(self, x, y):
        return self.data[y * self.width + x]

    def get_ascii(self, n):
        return str(self.data[n])

    def fill(self, c):
        self.data = [ copy(c) for i in range(self.width * self.height) ]


class Display(Board):
    def __init__(self, width, height):
        Board.__init__(self, width, height)
        self.data = [ Color() for i in range(width * height) ]

    def serialize(self):
        result = []

        for c in self.data:
            result += [int(c.r), int(c.g), int(c.b)]

        return result

    def get_ascii(self, x, y) :
        return str(int(self.get(x, y).get_brightness()) % 10)

    def print_ascii(self):
        buff = ""
        for y in range(self.height):
            for x in range(self.width):
                buff += self.get_ascii(x, y) + " "
            buff += "\n"
        print (buff)

    def fade(self, fade_factor):
        for c in self.data:
            c.fade(fade_factor)


if __name__ == "__main__":
    dis = Display(10, 10)
    dis.set(1,2, Color(3,3,3))
    dis.print_ascii()
