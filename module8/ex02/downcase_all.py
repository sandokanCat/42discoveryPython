#!/usr/bin/env python3

import sys

# DEFINE A METHOD TO CONVERT A STRING TO LOWERCASE
def downcase_it(s): return s.lower()

# CHECK IF PARAMETERS WERE PROVIDED
if len(sys.argv) == 1: print("none")

else:
    # APPLY downcase_it TO EACH PARAMETER
    for param in sys.argv[1:]:
        print(downcase_it(param))
