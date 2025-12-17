#!/usr/bin/env python3

# DISPLAY ALL PARAMETERS IN REVERSE ORDER OR "NONE" IF FEWER THAN 2

import sys

if len(sys.argv[1:]) < 2: print("none")  # NOT ENOUGH PARAMETERS
else:
    for p in reversed(sys.argv[1:]):  # ITERATE PARAMETERS BACKWARDS
        print(p)  # DISPLAY PARAMETER
