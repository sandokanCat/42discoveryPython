#!/usr/bin/env python3

try:
    user_num = int(input('Enter a number: '))
    init_num = 0

    while init_num <= 9:
        print(str(init_num) + ' x ' + str(user_num) + ' = ' + str(init_num * user_num))
        init_num += 1

except ValueError:
    print('Enter a valid number!')

        
