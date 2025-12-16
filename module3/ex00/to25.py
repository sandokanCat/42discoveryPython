#!/usr/bin/env python3

try:
    number = int(input('Enter a number less than 25: '))
    
    if number <= 25:
        while number <= 25:
            print('Inside the loop, my variable is ' + str(number))
            number += 1
    else:
        print('Error')

except ValueError:
    print('Enter a valid number!')
