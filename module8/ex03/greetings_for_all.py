#!/usr/bin/env python3

# DEFINE A GREETING METHOD WITH DEFAULT AND TYPE CHECK
def greetings(name="noble stranger"):
    if not isinstance(name, str): print("Error! It was not a name.")
    else: print(f"Hello, {name}.")

# TEST CALLS
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
