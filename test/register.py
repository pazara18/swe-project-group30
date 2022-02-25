import pyautogui as pg
from time import sleep

def press_key(key, n=1):
    for _ in range(n):
        pg.press(key)

sleep(3)

#14524657186
#cinlisifre

name = "Mert"
surname = "Kaya"
national_id = "14524657185"
age = "25"

# male : 0, female : 1
gender = 0

# white : 0, black : 1, asian : 2, hawaiian : 3, native : 4, other :5
race = 0
height = "180"
weight = "76"
password = "guclusifre"
c_password = "guclusifre"

# empty tests
# name : 0
# surname : 1
# age : 2
# height : 3
# weight : 4
# national_id : 5
# password : 6 
# confirm password : 7
# wrong tests
# password doesn't match : 8
# national_id is not 11 digits : 9
# alphabetic characters in national_id : 10
# successful register/user already exists : 11

# test_type = 0

for test_type in range(12):
    if test_type == 0:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write("")
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')

    elif test_type == 1:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write("")
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')

    elif test_type == 2:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write("")
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')

    elif test_type == 3:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write("")
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')
        
    elif test_type == 4:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write("")
        press_key('tab')

        press_key('enter')
        
    elif test_type == 5:
        press_key('tab', 4)
        pg.write("")
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')
        
    elif test_type == 6:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write("")
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')

    elif test_type == 7:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write("")
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')

    elif test_type == 8:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write("wrong confirm")
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')

    elif test_type == 9:
        press_key('tab', 4)
        pg.write("123")
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')

    elif test_type == 10:
        press_key('tab', 4)
        pg.write("asdasdasdas")
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')
    
    elif test_type == 11:
        press_key('tab', 4)
        pg.write(national_id)
        press_key('tab')
        pg.write(password)
        press_key('tab')
        pg.write(c_password)
        press_key('tab')
        pg.write(name)
        press_key('tab')
        pg.write(surname)
        press_key('tab')
        pg.write(age)
        press_key('tab')

        #select gender
        press_key('enter')
        for i in range(gender):
            press_key('down')
        press_key('enter')    
        press_key('tab')

        #select race
        press_key('enter')
        for i in range(race):
            press_key('down')
        press_key('enter')
        press_key('tab')

        pg.write(height)
        press_key('tab')
        pg.write(weight)
        press_key('tab')

        press_key('enter')
    

    sleep(5)