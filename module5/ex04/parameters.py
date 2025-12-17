#!/usr/bin/env python3

# COUNT AND DISPLAY NUMBER OF PARAMETERS PASSED TO SCRIPT

import sys

num_params = len(sys.argv) - 1  # CALCULATE NUMBER OF PARAMETERS (EXCLUDING SCRIPT NAME)

print(f"Number of parameters: {num_params}.")  # SHOW RESULT
