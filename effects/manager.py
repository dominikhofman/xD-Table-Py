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
from display import Color

class Manager(object):
    def __init__(self, bor):
        self.currnet_idx = 3
        texte = text.Text(bor)
        texte.set_text(10, 1, "SIEMA DANIEL XD")

        self.effects = [
            texte,
            pixels.Pixels(bor),
            rainbow.Rainbow(bor),
            sinrainbow2.SinRainbow2(bor),
            sinrainbow.SinRainbow(bor),
#            tetris.Tetris(10, 10),
            metaballs.Metaballs(bor),
            disco.Disco(),
            pulsingcolor.PulsingColor(Color(0,0,255)),
            solidcolor.SolidColor(Color(255,0,0)),
            solidcolor.SolidColor(Color(0,255,0)),
            solidcolor.SolidColor(Color(0,0,255)),
            solidcolor.SolidColor(Color(0,0,0)),
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
