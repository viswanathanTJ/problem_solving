import pyautogui as p
from time import sleep

with open('input.txt', 'r') as f:
    w = f.read()

p.hotkey('alt','tab')
sleep(.5)
p.typewrite(w)