#!/usr/bin/env python3

import sys

# VALIDATE EXACTLY ONE CLI ARGUMENT
if len(sys.argv) != 2: print("none")
else:
    parameter = sys.argv[1]  # CLI PARAMETER TO MATCH
    user_string = input("What was the parameter? ")  # USER INPUT

    # COMPARE USER INPUT WITH CLI PARAMETER
    if user_string == parameter: print("Good job!")
    else: print("Nope, sorry...")
