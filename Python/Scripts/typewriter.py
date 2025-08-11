import pyautogui as p
from time import sleep

p.hotkey('alt','tab')
sleep(.5)
with open('input.txt', 'r') as f:
    w = f.read()
p.typewrite(w)

## Remove extra brackets
# p.keyDown('shiftleft')
# p.keyDown('shiftright')
# p.press(['down']*10)
# p.keyUp('shiftleft')
# p.keyUp('shiftright')
# p.press('delete')
print('done')