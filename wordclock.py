import datetime
import time

from display_terminal import TerminalDisplay
from sentence_generator import SentenceGenerator

generator = SentenceGenerator()

display = TerminalDisplay()
display.init()

while True:
    now = datetime.datetime.now().time()
    sentence = generator.get_sentence(now)

    display.show_sentence(sentence)

    time.sleep(30)
