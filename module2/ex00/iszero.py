#!/usr/bin/env python3

try:
    number = int(input("Write a number: "))

    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")

except ValueError:
    print("Please enter a valid number.")

