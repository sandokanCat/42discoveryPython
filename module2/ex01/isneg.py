#!/usr/bin/env python3

try:
    number = int(input('Write a number: '))

    if number < 0:
        print('This number is negative.')
    elif number > 0:
        print('This number is positive.')
    else:
        print('This number is both positive and negative.')

except ValueError:
    print('Please enter a valid number.')

