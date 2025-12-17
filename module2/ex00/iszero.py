#!/usr/bin/env python3

# ASK USER FOR A NUMBER AND CHECK IF IT IS ZERO

try:
    number = int(input("Write a number: "))  # GET USER INPUT AND CONVERT TO INT

     # CHECK NUMBER VALUE
    if number == 0: print("This number is equal to zero.")  # NUMBER IS ZERO
    else: print("This number is different from zero.")  # NUMBER IS NOT ZERO

# HANDLE INVALID INPUT
except ValueError: print("Please enter a valid number.")
