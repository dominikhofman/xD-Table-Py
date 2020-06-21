import colorsys
from display import Color
from random import random
from PIL import Image, ImageSequence



class GifPlayer(object):
    def __init__(self, gif_path):
        im = Image.open(gif_path)
        if im.size != (10, 10):
            raise Exception('Wrong giff size! Expected 10x10 got %sx%s' % im.size)

        rgb_im = im.convert('RGB')

        self._current_frame_idx = 0
        self._frames = []

        for frame in ImageSequence.Iterator(im):
            self._frames.append(frame.convert('RGB'))

        self._dz = 8
        self._z = 0

    def step(self, dt):
        self._z += self._dz * dt
        self._current_frame_idx = int(self._z % len(self._frames))


    def render(self, display):
        current_frame = self._frames[self._current_frame_idx]
        for y in range(display.height):
            for x in range(display.width):
                display.set(x, y, Color(*current_frame.getpixel((x, y))))

def main():
    pass
    
if __name__ == "__main__":
    main()