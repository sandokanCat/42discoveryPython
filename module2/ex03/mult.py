#!/usr/bin/env python3

# MULTIPLICATION AND SIGN CHECK

try:
    first_num = int(input('Enter the first number: '))  # USER INPUT FIRST NUMBER
    second_num = int(input('Enter the second number: '))  # USER INPUT SECOND NUMBER
    mult = first_num * second_num  # CALCULATE MULTIPLICATION

    print(str(first_num) + ' x ' + str(second_num) + ' = ' + str(mult))  # SHOW RESULT

     # CHECK SIGN OF RESULT
    if mult > 0: print('The result is positive.')  # RESULT POSITIVE
    elif mult < 0: print('The result is negative.')  # RESULT NEGATIVE
    else: print('The result is positive and negative.')  # RESULT ZERO

# HANDLE INVALID INPUT
except ValueError: print('Enter a valid number!')
