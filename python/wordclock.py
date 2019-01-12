import datetime
import time
import threading
import sys

from display_terminal import TerminalDisplay
from sentence_generator import SentenceGenerator

generator = SentenceGenerator()
display = TerminalDisplay()

display.init()

color = (0, 255, 0)

def refresh_display():
    now = datetime.datetime.now().time()
    sentence = generator.get_sentence(now)

    display.color = color
    display.show_sentence(sentence)

def timed_refresh():
    try:
        refresh_display()
        threading.Timer(5.0, timed_refresh).start()
    except KeyboardInterrupt:
        sys.exit()

timed_refresh()
