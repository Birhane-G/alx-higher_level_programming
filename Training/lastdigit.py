#!/usr/bin/python3
import random
number = 90

if number >= 0:
    number2 = int(repr(number)[-1])
else:
    number2 = int(repr(number)[-1]) * -1

if number2 > 5:
    print(f"Last digit of {number} is {number2} and is greater than 5")
elif number2 < 6 and number2 != 0:
    print(f"Last digit of {number} is {number2} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {number2} and is 0")
