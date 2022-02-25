import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

test_type = 0 #0 valid patient id with data,1 valid patient id without data, 2 invalid patient id, 3 non-existent patient id, 4 invalid type 2 missing digits in patient id


if not test_type:
    national_id = "11111111111"
    press_key('tab',8)
    pg.write(national_id)
    press_key('tab')
    press_key('enter')
elif test_type==1:
    national_id = "12345678910"
    press_key('tab',8)
    pg.write(national_id)
    press_key('tab')
    press_key('enter')
elif test_type==2:
    national_id = "a1111111111"
    press_key('tab',8)
    pg.write(national_id)
    press_key('tab')
    press_key('enter')
elif test_type==3:
    national_id = "11111111112"
    press_key('tab',8)
    pg.write(national_id)
    press_key('tab')
    press_key('enter')
elif test_type==4:
    national_id = "1111111111"
    press_key('tab',8)
    pg.write(national_id)
    press_key('tab')
    press_key('enter')