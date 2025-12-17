#!/usr/bin/env python3

# AGE PROGRESSION CALCULATOR

age = int(input("Please tell me your age: "))  # USER INPUT AGE

print(f"You are currently {age} years old.")  # SHOW CURRENT AGE

i = 10
while i <= 30:
    print(f"In {i} years, you'll be {age + i} years old.")  # SHOW FUTURE AGE
    i += 10  # INCREMENT YEARS
