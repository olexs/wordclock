import datetime
import time

from test_display import TestDisplay
from sentence_generator import SentenceGenerator

generator = SentenceGenerator()

display = TestDisplay()
display.init()

while True:
    now = datetime.datetime.now().time()
    sentence = generator.get_sentence(now)

    display.show_sentence(sentence)

    time.sleep(30)
