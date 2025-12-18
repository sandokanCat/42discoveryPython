#!/usr/bin/env python3

import sys

# CHECK IF NO CLI PARAMETERS WERE PROVIDED
if len(sys.argv) == 1: print("none")
else:
    params = sys.argv[1:]  # EXTRACT CLI PARAMETERS ONLY

    # ITERATE OVER EACH PARAMETER
    for param in params:
        # SKIP WORDS ALREADY ENDING WITH 'ism'
        if param.find("ism") == len(param) - 3: continue

        # APPEND 'ism' AND PRINT RESULT
        print(f"{param}ism")
