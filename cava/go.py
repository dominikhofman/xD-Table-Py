import sys
sys.path.append('../utils')
from driver import Driver
from display import Display, Color
dr = Driver("192.168.1.214", 6454)

display = Display(10, 10)
pallette = [Color.hsv(i/22 + 0.5) for i in range(10)]

def draw_bar(x, height):
    for i in range(height + 1):
        display.set(x, i, pallette[i])

with open('cava.output') as f:
    while True:
        l = f.readline().strip().split(';')[10:-1]
        l = l[::-1]
        l = [int(i) for i in l]
        display.fill(Color.black())
        for i, c in enumerate(l):
            draw_bar(i, c)
        dr.set_matrix(display.serialize())
