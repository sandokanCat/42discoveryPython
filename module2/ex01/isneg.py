#!/usr/bin/env python3

# ASK USER FOR A NUMBER AND CHECK IF POSITIVE, NEGATIVE OR ZERO

try:
    number = int(input('Write a number: '))  # GET USER INPUT AND CONVERT TO INT

     # CHECK NUMBER SIGN
    if number < 0: print('This number is negative.')  # NUMBER IS NEGATIVE
    elif number > 0: print('This number is positive.')  # NUMBER IS POSITIVE
    else: print('This number is both positive and negative.')  # NUMBER IS ZERO

# HANDLE INVALID INPUT
except ValueError: print('Please enter a valid number.')
