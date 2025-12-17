#!/usr/bin/env python3

# DISPLAY FIRST PARAMETER IN LOWERCASE OR "NONE" IF NOT PROVIDED

import sys

if len(sys.argv) > 1: print(sys.argv[1].lower())  # SHOW PARAMETER IN LOWERCASE
else: print("none")  # NO PARAMETERS PASSED
