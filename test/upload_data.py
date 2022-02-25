import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

national_id = "14524657185"
#0-1
smoking = 0
r_rate = "10"
pain = "5"
h_rate = "79"
ldl = "100"
hdl = "110"
tri = "214"
hemoglobin = "154"
sodium = "1.7"
systolic = "8.7"
diastolic = "12.9"
#0-5
stress = 3

#enter national id
press_key('tab', 8)
pg.write(national_id)
press_key('tab')
press_key('enter')

#get to form
press_key('tab', 8)
pg.write(ldl)
press_key('tab')
pg.write(hdl)
press_key('tab')
pg.write(tri)
press_key('tab')
pg.write(hemoglobin)
press_key('tab')
pg.write(sodium)
press_key('tab')
pg.write(systolic)
press_key('tab')
pg.write(diastolic)
press_key('tab')
pg.write(h_rate)
press_key('tab')
pg.write(r_rate)
press_key('tab')
pg.write(pain)
press_key('tab')
press_key('enter')
for _ in range(smoking):
    press_key('down')
press_key('enter')
press_key('tab')
press_key('enter')
for _ in range(stress):
    press_key('down')
press_key('enter')
press_key('tab')
press_key('enter')


