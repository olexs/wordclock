import datetime
import json
import time
import threading
import os
import sys
import signal
from dotenv import load_dotenv

load_dotenv()

# check if we are running on a Raspberry Pi or on a local Windows/Mac machine
def is_raspberry_pi():
    try:
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if line.startswith('Hardware'):
                    _, value = line.strip().split(':', 1)
                    value = value.strip()
                    if value in ('BCM2708', 'BCM2709', 'BCM2835', 'BCM2836'):
                        return True
    except IOError:
        pass

    return False

if is_raspberry_pi():
    from display_driver import NeopixelDriver
    from display_neopixel import NeopixelDisplay
    display = NeopixelDisplay(NeopixelDriver())
    file_location = "/home/pi/wordclock/"
else:
    from display_terminal import TerminalDisplay
    display = TerminalDisplay()
    file_location = ""

from sentence_generator import SentenceGenerator

# ----- Saving color value in file -----

def load_color():
    configfile = open(file_location + "color.txt", "r")
    r = int(configfile.readline())
    g = int(configfile.readline())
    b = int(configfile.readline())
    brightness = int(configfile.readline())
    configfile.close()
    return r, g, b, brightness

def set_color():
    try:
        r, g, b, brightness = load_color()
        set_r, set_g, set_b = int(r * brightness / 255), int(g * brightness / 255), int(b * brightness / 255)
        print("Setting display RGB to", set_r, set_g, set_b)
        display.color = (set_r, set_g, set_b)
        client.publish(light_state_topic, json.dumps({
            "state": "ON" if brightness > 0 else "OFF", 
            "color": {"r": r, "g": g, "b": b},
            "brightness": brightness
        }))
    except:
        print("Error while loading saved color")
        
def save_color(color, brightness):
    configfile = open(file_location + "color.txt", "w")
    configfile.writelines(str(x) + '\n' for x in color)
    configfile.write(str(brightness) + '\n')
    configfile.close()
    set_color()

# ----- MQTT client handling -----

import paho.mqtt.client as mqtt

# MQTT settings
mqtt_broker = os.getenv("MQTT_BROKER")
mqtt_port = int(os.getenv("MQTT_PORT"))
mqtt_username = os.getenv("MQTT_USERNAME")
mqtt_password = os.getenv("MQTT_PASSWORD")

# Home Assistant MQTT discovery settings
ha_discovery_prefix = "homeassistant"
ha_discovery_topic = f"{ha_discovery_prefix}/light/wordclock/light/config"

# MQTT topics for RGB light
light_state_topic = "wordclock/light/state"
light_command_topic = "wordclock/light/command"

# MQTT client setup
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(mqtt_username, mqtt_password)

# MQTT callbacks
def on_connect(client, userdata, flags, rc, properties):
    client.publish(ha_discovery_topic, payload=json.dumps({
        "name": "Wordclock",
        "state_topic": light_state_topic,
        "command_topic": light_command_topic,
        "brightness": True,
        "rgb": True,
        "supported_color_modes": ["rgb"],
        "schema": "json"
    }), retain=True)
    client.subscribe(light_command_topic)

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)

    state = payload.get('state')
    brightness = payload.get('brightness')
    r, g, b = payload.get('color', {}).get('r'), payload.get('color', {}).get('g'), payload.get('color', {}).get('b')

    current_r, current_g, current_b, current_brightness = load_color()

    if state == "OFF":
        brightness = 0
        print("Turning off light")
    elif brightness is None:
        brightness = current_brightness
    else:
        print("Setting brightness to", brightness)

    if r is None and g is None and b is None:
        r, g, b = current_r, current_g, current_b
    else:
        print("Setting color to", r, g, b)

    save_color((r, g, b), brightness)
    refresh_display()  

client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT loop in a separate thread
client.loop_start()

# ----- SIGTERM handling -----

class GracefulKiller:
  kill_now = False

  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True

killer = GracefulKiller()

# ----- Wordclock display handling -----

generator = SentenceGenerator()

display.init()
set_color()

def refresh_display():
    now = datetime.datetime.now().time()
    sentence = generator.get_sentence(now)
    display.show_sentence(sentence)

def timed_refresh():
    if not killer.kill_now:
        refresh_display()
        threading.Timer(5.0, timed_refresh).start()

timed_refresh()

# ----- Main loop -----
try:
    while not killer.kill_now:
        time.sleep(1)
except KeyboardInterrupt:
    pass

