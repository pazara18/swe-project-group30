import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

# false : 0, true : 1
remember = 0
# # patient : 0, doctor : 1, manager : 2
user_type = 0
# wrong national_id : 0, wrong password : 1, wrong user_type : 2, successful login : 3
test_type = 3

if user_type == 0:
    national_id = "14524657185"
    password = "dahaguclusifre"

    # patient example
    # national_id = "14524657186"
    # password = "cinlisifre"

elif user_type == 1:
    # doctor example

    national_id = "16325564485"
    password = "FVVf_tRtw3UdVw"
    password = "dahaguclusifre"
else:
    # manager example

    national_id = "14567123975"
    password = "dahaguclusifre"

if test_type == 0:
    #wrong national id
    press_key('tab', 4)
    pg.write("11111111111")
    press_key('tab')
    pg.write(password)
    press_key('tab')

    press_key('enter')
    for i in range(user_type):
        press_key('down')
    press_key('enter')
    press_key('tab')

    if remember == 1:
        press_key('space')
    press_key('tab')
    press_key('enter')

elif test_type == 1:
    #wrong password 
    press_key('tab', 4)
    pg.write(national_id)
    press_key('tab')
    pg.write("wrong password")
    press_key('tab')

    press_key('enter')
    for i in range(user_type):
        press_key('down')
    press_key('enter')
    press_key('tab')

    if remember == 1:
        press_key('space')
    press_key('tab')
    press_key('enter')

elif test_type == 2:
    #wrong user type
    press_key('tab', 4)
    pg.write(national_id)
    press_key('tab')
    pg.write(password)
    press_key('tab')

    press_key('enter')
    for i in range(abs(user_type-1)):
        press_key('down')
    press_key('enter')
    press_key('tab')

    if remember == 1:
        press_key('space')
    press_key('tab')
    press_key('enter')

elif test_type == 3:
    #successful login
    press_key('tab', 4)
    pg.write(national_id)
    press_key('tab')
    pg.write(password)
    press_key('tab')

    press_key('enter')
    for i in range(user_type):
        press_key('down')
    press_key('enter')
    press_key('tab')

    if remember == 1:
        press_key('space')
    press_key('tab')
    press_key('enter')