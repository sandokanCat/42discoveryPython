#!/usr/bin/env python3

# CEILING OF A NUMBER

import math  # IMPORT MATH MODULE

try:
    num = float(input("Give me a number: "))  # USER INPUT

    print(math.ceil(num))  # PRINT CEILING VALUE

except ValueError: print("Please enter a valid number.")  # INVALID INPUT
