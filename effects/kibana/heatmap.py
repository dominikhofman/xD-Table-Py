import colorsys
from display import Color
from .kibana_heatmap_matrix import get_matrix
import time

class Heatmap(object):
    COLOR_PALETTE = {
            0: Color(247,251,255),
            1: Color(227,238,249),
            2: Color(208,225,242),
            3: Color(182,212,233),
            4: Color(148,196,223),
            5: Color(107,174,214),
            6: Color(74,152,201),
            7: Color(46,126,188),
            8: Color(23,100,171),
            9: Color(8,74,145),
            None: Color(0,0,0)
    }

    FETCH_INTERVAL = 5 * 60 # seconds
    ERROR_COOLOR = Color(128, 0, 0)

    def __init__(self):
        self._last_fetch = 0
        self._matrix = None
        pass
        # im = Image.open(gif_path)
        # if im.size != (10, 10):
        #     raise Exception('Wrong giff size! Expected 10x10 got %sx%s' % im.size)

        # rgb_im = im.convert('RGB')

        # self._current_frame_idx = 0
        # self._frames = []

        # for frame in ImageSequence.Iterator(im):
        #     self._frames.append(frame.convert('RGB'))

        # self._dz = 8
        # self._z = 0

    def step(self, dt):
        if time.time() - self._last_fetch > self.FETCH_INTERVAL:
            self._last_fetch = time.time()
            self._matrix = get_matrix()
            print('fetch')
        # self._z += self._dz * dt
        # self._current_frame_idx = int(self._z % len(self._frames))


    def render(self, display):
        if self._matrix is None:
           display.fill(Color(self.ERROR_COOLOR))
           return

        for y, row in enumerate(self._matrix):
            for x, color_idx in enumerate(row):
                display.safe_set(x, y, self.COLOR_PALETTE.get(color_idx, self.ERROR_COOLOR))

        # for y in range(display.height):
        #     for x in range(display.width):
        #         display.set(1, 0, self.COLOR_PALETTE.get(x, Color(100,0,0)))
