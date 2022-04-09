import pyautogui as pg
from time import sleep
import pyperclip

f = open('texts.txt', 'a')
pg.hotkey('alt', 'tab')
sleep(.5)
for _ in range(50):
    pg.press('home')
    pg.hotkey('shift', 'end')
    pg.hotkey('ctrl', 'c')
    f.writelines(pyperclip.paste()+'\n')
    pg.press('down')
