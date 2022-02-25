import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

test_type = True
height = "169"
wrong_height = "abc"

if test_type:
    press_key('tab', 8)
    press_key('enter')
    press_key('tab',2)
    pg.write(height)
    press_key('tab')
    press_key('enter')

else:
    press_key('tab', 8)
    press_key('enter')
    press_key('tab',2)
    pg.write(wrong_height)
    press_key('tab')
    press_key('enter')
