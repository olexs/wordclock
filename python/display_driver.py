import board
import neopixel

class NeopixelDriver:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 110)
        
    def get_pixels(self):
        return self.pixels