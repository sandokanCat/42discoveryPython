#!/usr/bin/env python3

import sys

# CHECK FOR EXACTLY ONE CLI PARAMETER
if len(sys.argv) != 2: print("none")
else:
    string = sys.argv[1]
    z_count = 0

    # ITERATE OVER EACH CHARACTER IN THE STRING
    for char in string:
        if char == "z":
            z_count += 1

    # PRINT RESULT BASED ON FOUND OCCURRENCES
    if z_count == 0: print("none")
    else: print("z" * z_count)
