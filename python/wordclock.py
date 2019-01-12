import datetime
import time
import threading

from display_terminal import TerminalDisplay
from sentence_generator import SentenceGenerator

generator = SentenceGenerator()
display = TerminalDisplay()

display.init()

def refresh_display():
    now = datetime.datetime.now().time()
    sentence = generator.get_sentence(now)

    display.show_sentence(sentence)

def timed_refresh():
    refresh_display()
    threading.Timer(30.0, timed_refresh).start()

timed_refresh()
