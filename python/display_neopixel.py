import math

class NeopixelDisplay:

    def __init__(self, driver):
        self.driver = driver

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

    color = (255, 0, 0)

    def init(self):
        pass

    def show_sentence(self, sentence):
        self.set_led_sequence(sentence)
        
    def set_led_sequence(self, sentence):
        self.driver.fill((0,0,0))
        for word in sentence:
            [line_index, [word_start, word_length]] = self.words[word]
            range_start = line_index * self.linelength
            if line_index % 2 == 0 or not self.lines_in_z_order:
                range_start = range_start + word_start
            else:
                range_start = range_start + self.linelength - (word_start + word_length)
            range_end = range_start + word_length
            self.driver.set_value(range_start, range_end, self.color)
        self.driver.show()