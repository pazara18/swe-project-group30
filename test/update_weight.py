import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

test_type = True
weight = "62"
wrong_weight = "xqc"

if test_type:
    press_key('tab', 9)
    press_key('enter')
    press_key('tab',1)
    pg.write(weight)
    press_key('tab')
    press_key('enter')

else:
    press_key('tab', 9)
    press_key('enter')
    press_key('tab',1)
    pg.write(wrong_weight)
    press_key('tab')
    press_key('enter')
