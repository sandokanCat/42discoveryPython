#!/usr/bin/env python3

# FILTER AND INCREMENT ARRAY

array = [2, 8, 9, 48, 8, 22, -12, 2]  # ORIGINAL ARRAY

# ADD 2 ONLY TO ELEMENTS GREATER THAN 5
new_array = [x + 2 for x in array if x > 5]

print(array)      # SHOW ORIGINAL ARRAY
print(new_array)  # SHOW FILTERED AND UPDATED ARRAY
