#!/usr/bin/env python3

try:
    user_input = input('What you gotta say? : ')

    while user_input != 'STOP':
        user_input = input('I got that! Anything else? : ')

except Exception as e:
    print(f'Error: {e}')
