import unittest
from datetime import time
from display_neopixel import NeopixelDisplay

class NeopixelDisplayTests(unittest.TestCase):

    def test_show_sentence_simple(self):
        # Arrange
        c = (16,0,0)
        driver = MockDriver()
        display = NeopixelDisplay(driver)
        display.color = c

        # Act
        display.show_sentence(["es", "ist"])

        # Assert
        x = (0,0,0)
        self.assertEqual([c,c,x,c,c,c,x], driver.pixels[0:7])

    def test_show_sentence_complex(self):
        # Arrange
        c = (16,0,0)
        driver = MockDriver()
        display = NeopixelDisplay(driver)
        display.color = c

        # Act
        display.show_sentence(["es", "ist", "zehn", "nach", "zwölf"])

        # Assert
        x = (0,0,0)
        self.assertEqual([c,c,x,c,c,c,x], driver.pixels[0:7])
        self.assertEqual([x,c,c,c,c,x], driver.pixels[17:23])
        self.assertEqual([x,c,c,c,c,x], driver.pixels[37:43])
        self.assertEqual([x,c,c,c,c,c,x], driver.pixels[48:55])

class MockDriver:
    def __init__(self):
        self.pixels = [None] * 110

    def show(self):
        pass

    def fill(self, color):
        self.pixels = [color] * 110

    def set_value(self, start, end, color):
        self.pixels[start:end] = [color] * (end - start)

if __name__ == '__main__':
    unittest.main()