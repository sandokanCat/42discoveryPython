#!/usr/bin/env python3

# DISPLAY FIRST PARAMETER IN UPPERCASE OR "NONE" IF NOT PROVIDED

import sys

if len(sys.argv) > 1:print(sys.argv[1].upper())  # SHOW PARAMETER IN UPPERCASE
else: print("none")  # NO PARAMETERS PASSED
