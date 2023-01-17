#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    str1 = 'and is greater than 5'
    print(f'Last digit of {number} is {last_digit} {str1}')
elif last_digit == 0:
    str2 = 'and is 0'
    print(f'Last digit of {number} is {last_digit} {str2}')
elif last_digit < 6 and last_digit != 0:
    str3 = 'and is less than 6 and not 0'
    print(f'Last digit of {number} is {last_digit} {str3}')
