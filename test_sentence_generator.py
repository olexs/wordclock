import datetime
import unittest
from sentence_generator import SentenceGenerator

class SentenceGeneratorTests(unittest.TestCase):

    def test_get_sentence(self):
        # arrange
        gen = SentenceGenerator()

        # act, assert
        self.assertEqual('es ist zwölf uhr'.split(' '), gen.get_sentence(datetime.time(12, 0)))
        self.assertEqual('es ist zwölf uhr'.split(' '), gen.get_sentence(datetime.time(0, 0)))
        self.assertEqual('es ist sechs uhr'.split(' '), gen.get_sentence(datetime.time(6, 0, 0)))
        self.assertEqual('es ist sechs uhr'.split(' '), gen.get_sentence(datetime.time(18, 0, 0)))
        self.assertEqual('es ist fünf nach eins'.split(' '), gen.get_sentence(datetime.time(1, 5)))
        self.assertEqual('es ist zehn nach zwei'.split(' '), gen.get_sentence(datetime.time(2, 11)))
        self.assertEqual('es ist viertel nach drei'.split(' '), gen.get_sentence(datetime.time(3, 14)))
        self.assertEqual('es ist zwanzig nach vier'.split(' '), gen.get_sentence(datetime.time(4, 22)))
        self.assertEqual('es ist fünf vor halb fünf2'.split(' '), gen.get_sentence(datetime.time(4, 25)))
        self.assertEqual('es ist halb sechs'.split(' '), gen.get_sentence(datetime.time(5, 30, 0)))
        self.assertEqual('es ist fünf nach halb sieben'.split(' '), gen.get_sentence(datetime.time(6, 34, 0)))
        self.assertEqual('es ist zwanzig vor acht'.split(' '), gen.get_sentence(datetime.time(7, 42, 0)))
        self.assertEqual('es ist viertel vor neun'.split(' '), gen.get_sentence(datetime.time(20, 45, 0)))
        self.assertEqual('es ist zehn vor zehn2'.split(' '), gen.get_sentence(datetime.time(21, 49, 0)))
        self.assertEqual('es ist fünf vor elf'.split(' '), gen.get_sentence(datetime.time(10, 55, 0)))
        self.assertEqual('es ist fünf vor eins'.split(' '), gen.get_sentence(datetime.time(12, 55)))

if __name__ == '__main__':
    unittest.main()