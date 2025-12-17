#!/usr/bin/env python3

# ARRAY INCREMENT EXAMPLE

array = [2, 8, 9, 48, 8, 22, -12, 2]  # ORIGINAL ARRAY

new_array = [x + 2 for x in array]  # ADD 2 TO EACH ELEMENT

# SHOW BOTH ARRAYS
print(f"""Original array: {array}
New array: {new_array}""")
