# times_table.py
# CS 1 demo by THC to show nested while loops.
# Also shows how to right justify a string.

N = 10  # times table goes 1 to N-1

max_value = (N - 1) * (N - 1)           # max value computed
field_width = 1 + len(str(max_value))   # field width for right justifying

row = 1

while row < N:     # the header for the outer loop
    column = 1
    while column < N:   # the header for the inner loop
        print(str(row * column).rjust(field_width), end = '')
        column += 1

    print("")

    row += 1
