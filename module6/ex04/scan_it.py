#!/usr/bin/env python3

# COUNT OCCURRENCES OF A KEYWORD IN A STRING OR DISPLAY "NONE"

import sys
import re

if len(sys.argv[1:]) != 2: print("none")  # INVALID NUMBER OF PARAMETERS
else:
    keyword, text = sys.argv[1:]  # UNPACK PARAMETERS
    matches = re.findall(r'\b{}\b'.format(re.escape(keyword)), text)  # FIND WHOLE WORD MATCHES
    
    if matches: print(len(matches))  # DISPLAY NUMBER OF OCCURRENCES
    else: print("none")  # KEYWORD NOT FOUND
