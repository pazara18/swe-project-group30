import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

name = "cem"
surname = "akalin"
national_id = "16325564485"
c_national_id = "16325564485"
hospital_id = "131"
expertise = "cardiac surgeon"

#empty tests
#name : 0
#surname : 1
#national_id : 2
#confirm national_id : 3
#hospital_id : 4
#expertise : 5
#wrong tests
#confirm doesn't match : 6
#national_id has alphabetic characters : 7
#successful addition : 8

for test_type in range(9):
    if test_type == 0:
        press_key('tab', 6)
        pg.write("")
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        pg.write(expertise)
        press_key('tab')
        press_key('enter')
    elif test_type == 1:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write("")
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        pg.write(expertise)
        press_key('tab')
        press_key('enter')
    elif test_type == 2:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write("")
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        pg.write(expertise)
        press_key('tab')
        press_key('enter')
    elif test_type == 3:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write("")
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        pg.write(expertise)
        press_key('tab')
        press_key('enter')
    elif test_type == 4:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write("")
        press_key('tab')
        pg.write(expertise)
        press_key('tab')
        press_key('enter')
    elif test_type == 5:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        pg.write("")
        press_key('tab')
        press_key('enter')
    elif test_type == 6:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write("11111111111")
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        pg.write(expertise)
        press_key('tab')
        press_key('enter')
    elif test_type == 7:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write("asdasdasdas")
        press_key('tab')
        pg.write("asdasdasdas")
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        pg.write(expertise)
        press_key('tab')
        press_key('enter')
    elif test_type == 8:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        pg.write(expertise)
        press_key('tab')
        press_key('enter')

    sleep(5)
#pass
#FVVf_tRtw3UdVw