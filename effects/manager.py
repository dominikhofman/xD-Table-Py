#import tetris.tetris as tetris
#import .text.text as text
import text.text as text
import rainbow
import pixels
import metaballs
import solidcolor
import pulsingcolor
import disco
import sinrainbow
import sinrainbow2
import droplet
import paint
import tennis
from display import Color

class Manager(object):
    def __init__(self, bor):
        self.currnet_idx = 3
        texte = text.Text(bor)
        texte.set_text(10, 1, "SIEMA DANIEL XD")

        self.effects = [
            texte, # 0
            pixels.Pixels(bor), #1
            rainbow.Rainbow(bor), #2
            sinrainbow2.SinRainbow2(bor), #3
            sinrainbow.SinRainbow(bor), #4
#            tetris.Tetris(10, 10),
            metaballs.Metaballs(bor), #5
            disco.Disco(), #6
            pulsingcolor.PulsingColor(Color.blue()), #7
            solidcolor.SolidColor(Color.red()), #8
            solidcolor.SolidColor(Color.green()), #9
            solidcolor.SolidColor(Color.blue()), #10
            solidcolor.SolidColor(Color.black()), #11
            droplet.Droplet(bor), #12
            paint.Paint(bor), #13
            tennis.Tennis(bor), #13
        ]

    def next(self):
        self.currnet_idx += 1
        self.currnet_idx %= len(self.effects)

    def prev(self):
        self.currnet_idx -= 1
        self.currnet_idx %= len(self.effects)

    def get(self):
        return self.effects[self.currnet_idx]

    def set(self, idx):
        self.currnet_idx = idx

    def on_press(self, key):
        self.effects[self.currnet_idx].on_press(key)
