#!/usr/bin/env python3

# DEFINE A METHOD TO FIND FAMILY MEMBERS WITH RED HAIR USING FILTER
def find_the_redheads(family_dict):
    # FILTER KEYS WHERE VALUE IS 'red' AND CONVERT TO LIST
    return list(filter(lambda name: family_dict[name] == "red", family_dict.keys()))

# EXAMPLE USAGE
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
