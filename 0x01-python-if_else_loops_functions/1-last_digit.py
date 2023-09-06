#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = str(number)
if number < 0:
    value = "-" + value[-1:]
else:
    value = value[-1:]
if int(value) > 5:
    print(f"Last digit of {number} is {value} and is greater than 5")
elif int(value) == 0:
    print(f"Last digit of {number} is {value} and is 0")
elif int(value) < 6:
    print(f"Last digit of {number} is {value} and is less than 6 and not 0")
