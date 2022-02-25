import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

#empty tests
#name : 0
#surname : 1
#national_id : 2
#confirm national_id : 3
#hospital_id : 4
#wrong tests
#name : 5
#surname : 6
#national_id : 7
#hospital_id : 8
#national_id's doesn't match : 9
#successful activation : 10

name = "cem"
surname = "akalin"
national_id = "16325564485"
c_national_id = "16325564485"
hospital_id = "131"

for test_type in range(11):
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
        press_key('enter')
    if test_type == 1:
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
        press_key('enter')
    if test_type == 2:
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
        press_key('enter')
    if test_type == 3:
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
        press_key('enter')
    if test_type == 4:
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
        press_key('enter')

    if test_type == 5:
        press_key('tab', 6)
        pg.write("wrong name")
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        press_key('enter')

    if test_type == 6:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write("wrong surname")
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        press_key('enter')
    
    if test_type == 7:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write("11111111111")
        press_key('tab')
        pg.write("11111111111")
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        press_key('enter')

    if test_type == 8:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write(c_national_id)
        press_key('tab')
        pg.write("1000")
        press_key('tab')
        press_key('enter')
    
    if test_type == 9:
        press_key('tab', 6)
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(national_id)
        press_key('tab')
        pg.write("wrong confirm")
        press_key('tab')
        pg.write(hospital_id)
        press_key('tab')
        press_key('enter')
    
    if test_type == 10:
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
        press_key('enter')
    
    sleep(5)