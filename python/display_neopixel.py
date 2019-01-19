import math
import board
import neopixel

class NeopixelDisplay:

    display = [
        "ESKISTLFÜNF",
        "ZEHNZWANZIG",
        "DREIVIERTEL",
        "TGNACHVORJM",
        "HALBQZWÖLFP",
        "ZWEINSIEBEN",
        "KDREIRHFÜNF",
        "ELFNEUNVIER",
        "WACHTZEHNRS",
        "BSECHSFMUHR"
    ]

    lines_in_z_order = True

    linelength = len(display[0])
    led_count = linelength * len(display)

    words = {
        "es":           [0, [0, 2]],
        "ist":          [0, [3, 3]],
        "fünf":         [0, [7, 4]],
        "zehn":         [1, [0, 4]],
        "zwanzig":      [1, [4, 7]],
        "dreiviertel":  [2, [0, 11]],
        "viertel":      [2, [4, 7]],
        "nach":         [3, [2, 4]],
        "vor":          [3, [6, 3]],
        "halb":         [4, [0, 4]],
        "zwölf":        [4, [5, 5]],
        "zwei":         [5, [0, 4]],
        "eins":         [5, [2, 4]],
        "sieben":       [5, [5, 6]],
        "drei":         [6, [1, 4]],
        "fünf2":        [6, [7, 4]],
        "elf":          [7, [0, 3]],
        "neun":         [7, [3, 4]],
        "vier":         [7, [7, 4]],
        "acht":         [8, [1, 4]],
        "zehn2":        [8, [5, 4]],
        "sechs":        [9, [1, 5]],
        "uhr":          [9, [8, 3]]
    }

    color = (32, 0, 0)

    def init(self):
        self.pixels = neopixel.NeoPixel(board.D18, self.led_count)
        # todo: light up all LEDs

    def show_sentence(self, sentence):
        leds = self.get_led_sequence(sentence)
        self.show_leds(leds)

    def get_led_sequence(self, sentence):
        leds = []
        for word in sentence:
            line_index = self.words[word][0]
            word_start = self.words[word][1][0]
            word_length = self.words[word][1][1]
            range_start = line_index * self.linelength + word_start
            range_end = range_start + word_length
            leds = leds + list(range(range_start, range_end))
        return leds

    def show_leds(self, leds):
        line_index = 0
        for line in self.display:
            letter_index = 0
            for _ in line:
                led_index = (line_index * self.linelength) + letter_index
                led_color = self.color if led_index in leds else (0, 0, 0)
                if self.lines_in_z_order and line_index % 2 == 1: # every second line inverted in hardware
                    led_index = (line_index * self.linelength) + (self.linelength - letter_index - 1)
                self.pixels[led_index] = led_color
                letter_index = letter_index + 1
            line_index = line_index + 1
            