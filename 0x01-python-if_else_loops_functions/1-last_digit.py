#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = str(number)
if int(value[-1:]) > 5:
    print(f"Last digit of {number} is {value[-1:]} and is greater than 5")
elif int(value[-1:]) == 0:
    print(f"Last digit of {number} is {value[-1:]} and is 0")
else:
    print(f"Last digit of {number} is {value[-1:]} and is less than 6 and not 0")
