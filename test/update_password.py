import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

# patient : 0, doctor : 1, manager : 2
user_type = 0
# wrong old_password : 0, password and confirm different : 1, successful change : 2
test_type = 0

if user_type == 0:
    old_password = "Ac9SB7UVkRQqqw"
    password = "dahaguclusifre"
    confirm = "dahaguclusifre"
elif user_type == 1:
    old_password = "Ac9SB7UVkRQqqw"
    password = "dahaguclusifre"
    confirm = "dahaguclusifre"
elif user_type == 2:
    old_password = "Ac9SB7UVkRQqqw"
    password = "dahaguclusifre"
    confirm = "dahaguclusifre"

if test_type == 0:
    if user_type == 0:
        press_key('tab', 7)
    elif user_type == 1:
        press_key('tab', 8)
    if user_type == 2:
        press_key('tab', 6)
    press_key('enter')
    press_key('tab')
    pg.write(old_password + 'w')
    press_key('tab')
    pg.write(password)
    press_key('tab')
    pg.write(confirm)
    press_key('tab')
    press_key('enter')

elif test_type == 1:
    if user_type == 0:
        press_key('tab', 7)
    elif user_type == 1:
        press_key('tab', 8)
    if user_type == 2:
        press_key('tab', 6)
    press_key('enter')
    press_key('tab')
    pg.write(old_password)
    press_key('tab')
    pg.write(password + 'd')
    press_key('tab')
    pg.write(confirm)
    press_key('tab')
    press_key('enter')

elif test_type == 2:
    if user_type == 0:
        press_key('tab', 7)
    elif user_type == 1:
        press_key('tab', 8)
    if user_type == 2:
        press_key('tab', 6)
    press_key('enter')
    press_key('tab')
    pg.write(old_password)
    press_key('tab')
    pg.write(password)
    press_key('tab')
    pg.write(confirm)
    press_key('tab')
    press_key('enter')