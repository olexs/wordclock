import unittest
from datetime import time
from sentence_generator import SentenceGenerator

class SentenceGeneratorTests(unittest.TestCase):

    def test_get_sentence(self):
        # arrange
        gen = SentenceGenerator()

        # act, assert
        self.assertEqual('es ist zwölf uhr'.split(' '), gen.get_sentence(time(12, 0)))
        self.assertEqual('es ist zwölf uhr'.split(' '), gen.get_sentence(time(0, 0)))
        self.assertEqual('es ist sechs uhr'.split(' '), gen.get_sentence(time(6, 0)))
        self.assertEqual('es ist sechs uhr'.split(' '), gen.get_sentence(time(18, 0)))
        self.assertEqual('es ist fünf nach eins'.split(' '), gen.get_sentence(time(1, 5)))
        self.assertEqual('es ist zehn nach zwei'.split(' '), gen.get_sentence(time(2, 11)))
        self.assertEqual('es ist viertel nach drei'.split(' '), gen.get_sentence(time(3, 14)))
        self.assertEqual('es ist zwanzig nach vier'.split(' '), gen.get_sentence(time(4, 22)))
        self.assertEqual('es ist fünf vor halb fünf2'.split(' '), gen.get_sentence(time(4, 25)))
        self.assertEqual('es ist halb sechs'.split(' '), gen.get_sentence(time(5, 30)))
        self.assertEqual('es ist fünf nach halb sieben'.split(' '), gen.get_sentence(time(6, 34)))
        self.assertEqual('es ist zwanzig vor acht'.split(' '), gen.get_sentence(time(7, 42)))
        self.assertEqual('es ist viertel vor neun'.split(' '), gen.get_sentence(time(20, 45)))
        self.assertEqual('es ist zehn vor zehn2'.split(' '), gen.get_sentence(time(21, 49)))
        self.assertEqual('es ist fünf vor elf'.split(' '), gen.get_sentence(time(10, 55)))
        self.assertEqual('es ist fünf vor eins'.split(' '), gen.get_sentence(time(12, 55)))

if __name__ == '__main__':
    unittest.main()