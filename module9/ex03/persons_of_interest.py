#!/usr/bin/env python3

# DEFINE A METHOD TO DISPLAY HISTORICAL FIGURES SORTED BY BIRTH DATE
def famous_births(figures_dict):
    # SORT KEYS BASED ON 'date_of_birth' VALUE
    sorted_keys = sorted(figures_dict, key=lambda k: figures_dict[k]['date_of_birth'])

    # ITERATE OVER SORTED KEYS AND PRINT FORMATTED STRING
    for key in sorted_keys:
        info = figures_dict[key]
        print(f"{info['name']} is a great scientist born in {info['date_of_birth']}.")

# EXAMPLE USAGE
women_scientists = {
    "ada": {
        "name": "Ada Lovelace",
        "date_of_birth": "1815"
    },
    "cecilia": {
        "name": "Cecila Payne",
        "date_of_birth": "1900"
    },
    "lise": {
        "name": "Lise Meitner",
        "date_of_birth": "1878"
    },
    "grace": {
        "name": "Grace Hopper",
        "date_of_birth": "1906"
    }
}

famous_births(women_scientists)
