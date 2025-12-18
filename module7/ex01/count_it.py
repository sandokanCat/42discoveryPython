#!/usr/bin/env python3

import sys

# CHECK IF NO CLI PARAMETERS WERE PROVIDED
if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]  # EXTRACT CLI PARAMETERS ONLY

    print(f"parameters: {len(params)}")

    # ITERATE OVER EACH PARAMETER AND PRINT ITS LENGTH
    for param in params:
        print(f"{param}: {len(param)}")
