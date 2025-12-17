#!/usr/bin/env python3

# DISPLAY FIRST PARAMETER OR "NONE" IF NOT PROVIDED

import sys

if len(sys.argv) > 1: print(sys.argv[1])  # SHOW FIRST PARAMETER
else: print("none")  # NO PARAMETERS PASSED
