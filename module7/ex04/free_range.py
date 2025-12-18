#!/usr/bin/env python3

import sys

# CHECK FOR EXACTLY TWO CLI PARAMETERS
if len(sys.argv) != 3: print("none")
else:
    try:
        start = int(sys.argv[1])  # FIRST NUMBER
        end = int(sys.argv[2])    # SECOND NUMBER

        # VALIDATE ORDER
        if start > end: print("none")
        else:
            # CREATE ARRAY USING RANGE (INCLUSIVE)
            numbers = list(range(start, end + 1))
            print(numbers)

    # HANDLE NON-INTEGER INPUTS
    except ValueError: print("none")
