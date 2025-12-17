#!/usr/bin/env python3

# LOOP UNTIL NUMBER REACHES 25

try:
    number = int(input('Enter a number less than 25: '))  # USER INPUT

    if number <= 25:
         # LOOP CONDITION
        while number <= 25:
            print('Inside the loop, my variable is ' + str(number))  # SHOW CURRENT VALUE
            number += 1  # INCREMENT NUMBER
    else: print('Error')  # INPUT GREATER THAN 25

# HANDLE INVALID INPUT
except ValueError: print('Enter a valid number!')
