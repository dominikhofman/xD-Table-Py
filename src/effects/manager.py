#import tetris.tetris as tetris
# import .text.text as text
import effects.text.text as text
import effects.rainbow as rainbow
import effects.rainbow_slow as rainbow_slow
import effects.pixels as pixels
import effects.metaballs as metaballs
import effects.solidcolor as solidcolor
import effects.pulsingcolor as pulsingcolor
import effects.disco as disco
import effects.sinrainbow as sinrainbow
import effects.sinrainbow2 as sinrainbow2
import effects.droplet as droplet
import effects.paint as paint
import effects.tennis as tennis
import effects.rays as rays
import effects.plasma as plasma
import effects.xdcolor as xdcolor
import effects.kibana as kibana
from utils.display import Color
from effects.gifplayer import GifPlayer

class Manager(object):
    def __init__(self, bor):
        self.currnet_idx = 20
        # self.currnet_idx = 19
        texte = text.Text(bor)
        texte.set_text(10, 1, "XD XD XD XD")

        self.effects = [
            texte,  # 0
            pixels.Pixels(bor),  # 1
            rainbow.Rainbow(bor),  # 2
            sinrainbow2.SinRainbow2(bor),  # 3
            sinrainbow.SinRainbow(bor),  # 4
            #            tetris.Tetris(10, 10),
            metaballs.Metaballs(bor),  # 5
            disco.Disco(),  # 6
            pulsingcolor.PulsingColor(Color.blue()),  # 7
            xdcolor.XDColor(Color.red()),  # 8
            xdcolor.XDColor(Color.green()),  # 9
            xdcolor.XDColor(Color.blue()),  # 10
            solidcolor.SolidColor(Color.black()),  # 11
            droplet.Droplet(bor),  # 12
            paint.Paint(bor),  # 13
            tennis.Tennis(bor),  # 14
            rays.Rays(bor),  # 15
            plasma.Plasma(bor),  # 16
            #GifPlayer('/home/pi/xD-Table-Py/effects/gifplayer/gifs/fireplace_smol.gif'),  # 17
            GifPlayer('./effects/gifplayer/gifs/fireplace_doniel.gif'),  # 17
            rainbow_slow.RainbowSlow(bor),  # 18
            kibana.Heatmap(),  # 19

            # xdcolor.XDColor(Color(0xff, 0xff, 0x00)),  # 10

            # GifPlayer('/home/pi/hotline1.gif', fps=12),  # 20

            # GifPlayer('/home/pi/test9.gif', fps=12),  # 20
            plasma.Plasma(bor),  # 16

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
        idx = idx % len(self.effects)
        self.currnet_idx = idx

    def on_press(self, key):
        self.effects[self.currnet_idx].on_press(key)
