#!/usr/bin/env python3

import sys
import re

if len(sys.argv[1:]) != 2: print("none")
else:
    keyword, text = sys.argv[1:]
    matches = re.findall(r'\b{}\b'.format(re.escape(keyword)), text)
    
    if matches: print(len(matches))
    else: print("none")
