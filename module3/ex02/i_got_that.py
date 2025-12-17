#!/usr/bin/env python3

# SIMPLE LOOP UNTIL USER TYPES "STOP"

try:
    user_input = input('What you gotta say? : ')  # USER INPUT

     # LOOP UNTIL STOP
    while user_input != 'STOP': user_input = input('I got that! Anything else? : ')  # ASK AGAIN

# CATCH ANY ERROR
except Exception as e: print(f'Error: {e}')  # SHOW ERROR
