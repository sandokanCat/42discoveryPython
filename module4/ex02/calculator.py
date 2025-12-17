#!/usr/bin/env python3

# BASIC ARITHMETIC OPERATIONS

num1 = float(input("Give me the first number: "))  # USER INPUT FIRST NUMBER
num2 = float(input("Give me the second number: "))  # USER INPUT SECOND NUMBER

# SHOW SUM, SUBTRACTION, DIVISION, MULTIPLICATION
print(f"""Thank you!
{num1:g} + {num2:g} = {(num1 + num2):g}
{num1:g} - {num2:g} = {(num1 - num2):g}
{num1:g} / {num2:g} = {(num1 / num2):g}
{num1:g} * {num2:g} = {(num1 * num2):g}""")
