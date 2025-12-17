#!/usr/bin/env python3

# MULTIPLICATION TABLE FROM 0 TO 9

try:
    user_num = int(input('Enter a number: '))  # USER INPUT
    counter = 0  # STARTING NUMBER

     # LOOP FROM 0 TO 9
    while counter <= 9:
        print(str(counter) + ' x ' + str(user_num) + ' = ' + str(counter * user_num))  # SHOW MULTIPLICATION
        counter += 1  # INCREMENT COUNTER

# HANDLE INVALID INPUT
except ValueError: print('Enter a valid number!')
