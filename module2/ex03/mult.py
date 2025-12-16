#!/usr/bin/env python3

try:
    first_num = int(input('Enter the first number: '))
    second_num = int(input('Enter the second number: '))
    mult = first_num * second_num

    print(str(first_num) + ' x ' + str(second_num) + ' = ' + str(mult))

    if mult > 0:
        print('The result is positive.')
    elif mult < 0:
        print('The result is negative.')
    else:
        print('The result is positive and negative.')

except ValueError:
    print('Enter a valid number.')
