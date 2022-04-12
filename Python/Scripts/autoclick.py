from gettext import find
import keyboard
import pyautogui as pg
from time import sleep

'''
f to find
v to ocr
x to next
q to tab
'''

def run():
    keyboard.read_key()


def fun():
    pg.hotkey('ctrl', 'tab')
    pg.hotkey('ctrl', 'f')
    pg.hotkey('ctrl', 'v')
    sleep(.3)


def tabber():
    pg.hotkey('ctrl', 'tab')
    sleep(.3)


def space():
    pg.hotkey('ctrl', 'space')
    sleep(.3)


def next():
    pg.click(1425, 985)
    sleep(.3)
    pg.click(18, 409)


def my_exit():
    print('Exiting')
    quit()


keyboard.add_hotkey('f', fun)
keyboard.add_hotkey('q', tabber)
keyboard.add_hotkey('x', next)
keyboard.add_hotkey('v', space)
keyboard.add_hotkey('esc', my_exit)

while True:
    run()
