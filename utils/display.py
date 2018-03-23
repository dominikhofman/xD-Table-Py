from itertools import chain
from copy import copy
import colorsys

class Color(object):
    def __init__(self, r=0, g=0, b=0):
        self.r, self.g, self.b = r, g, b

    def __getitem__(self, n):
        if n == 0: return self.r
        if n == 1: return self.g
        if n == 2: return self.b

    def get_brightness(self):
        return (self.r + self.g + self.b) / 3.0

    def clone(self):
        return copy(self)

    def fade(self, factor):
        self.r *= factor
        self.g *= factor
        self.b *= factor
        return self

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
        return self

    def __eq__(self, other):
        if self.r != other.r:
            return False

        if self.g != other.g:
            return False

        if self.b != other.b:
            return False
        return True

    def __ne__(self, other):
        if self.r != other.r:
            return True

        if self.g != other.g:
            return True

        if self.b != other.b:
            return True
        return False

    def __str__(self):
        return "<r: {r}, g: {g}, b: {b}".format(**self.__dict__)

    @staticmethod
    def hsv(h, s=1.0, v=255):
        return Color(*colorsys.hsv_to_rgb(h, s, v))

    @staticmethod
    def black():
        return Color(0, 0, 0)

    @staticmethod
    def white():
        return Color(255, 255, 255)

    @staticmethod
    def red():
        return Color(255, 0, 0)

    @staticmethod
    def green():
        return Color(0, 255, 0)

    @staticmethod
    def blue():
        return Color(0, 0, 255)

class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [ 0 for i in range(width * height) ]

    def set(self, x, y, c):
        self.data[y * self.width + x] = c

    def safe_set(self, x, y, c):
        x = int(x)
        y = int(y)
        if x > self.width - 1 or x < 0:
            return
        if y > self.height - 1 or y < 0:
            return

        self.data[y * self.width + x] = c

    def get(self, x, y):
        return self.data[y * self.width + x]

    def safe_get(self, x, y):
        x = int(x)
        y = int(y)
        if x > self.width - 1 or x < 0:
            return Color.black()
        if y > self.height - 1 or x < 0:
            return Color.black()

        return self.data[y * self.width + x]


    def row(self, y):
        return self.data[ self.width * y : self.width * (y + 1) ]

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
