import datetime
import time
import threading
import os
import sys
from flask import Flask, render_template, jsonify, request

if (os.name == 'nt'):
    from display_terminal import TerminalDisplay
    display = TerminalDisplay()
else:
    from display_driver import NeopixelDriver
    from display_neopixel import NeopixelDisplay
    display = NeopixelDisplay(NeopixelDriver())

from sentence_generator import SentenceGenerator

# ----- Wordclock display handling -----

generator = SentenceGenerator()


display.init()

def refresh_display():
    now = datetime.datetime.now().time()
    sentence = generator.get_sentence(now)

    display.show_sentence(sentence)

def timed_refresh():
    try:
        refresh_display()
        threading.Timer(5.0, timed_refresh).start()
    except KeyboardInterrupt:
        sys.exit()

timed_refresh()

# ----- Remote controller application -----

app = Flask(__name__, template_folder='templates')

@app.route('/')
def remote():
    return render_template('remote.html')

@app.route('/setcolor', methods=['POST'])
def set_color():
    r = int(request.args.get('r'))
    g = int(request.args.get('g'))
    b = int(request.args.get('b'))
    display.color = (r, g, b)
    refresh_display()
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)