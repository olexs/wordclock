import board
import neopixel

class NeopixelDriver:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 110, auto_write = False)
        
    def show(self):
        self.pixels.show()

    def fill(self, color):
        self.pixels.fill(color)

    def set_value(self, start, end, color):
        self.pixels[start:end] = [color] * (end - start)