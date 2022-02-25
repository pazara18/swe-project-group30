import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

# wrong national_id : 0 correct national_id: 1
test_type = 0

if test_type == 0:
    national_id = "14524657143"
    diagnosis = "covid-19"

    press_key('tab', 9)
    pg.write(national_id)
    press_key('tab')
    press_key('enter')
    press_key('tab', 9)
    pg.write(diagnosis)
    press_key('tab')
    press_key('enter')

elif test_type == 1:
    national_id = "14524657185"
    diagnosis = "covid-19"

    press_key('tab', 9)
    pg.write(national_id)
    press_key('tab')
    press_key('enter')
    press_key('tab', 9)
    pg.write(diagnosis)
    press_key('tab')
    press_key('enter')