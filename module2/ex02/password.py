#!/usr/bin/env python3

# SIMPLE PASSWORD CHECK

password = 'Python is awesome'  # SET CORRECT PASSWORD
user_pass = input('Enter your password: ')  # ASK USER FOR PASSWORD

# CHECK IF INPUT MATCHES PASSWORD
if user_pass == password: print('ACCESS GRANTED')  # PASSWORD CORRECT
else: print('ACCESS DENIED')  # PASSWORD INCORRECT
