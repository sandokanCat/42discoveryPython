#!/usr/bin/env python3

# MULTIPLICATION TABLE 0 TO 10

r = 0
while r <= 10:  # OUTER LOOP FOR ROWS
    print(f'Table of {r}:', end=' ')  # SHOW ROW HEADER

    c = 0
    while c <= 10:  # INNER LOOP FOR COLUMNS
        print(r * c, end=' ')  # PRINT MULTIPLICATION
        c += 1

    print()  # NEWLINE AFTER ROW
    r += 1  # NEXT ROW
