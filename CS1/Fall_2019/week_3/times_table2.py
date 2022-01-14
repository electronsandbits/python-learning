# times_table2.py
# CS 1 demo by THC to show nested for loops.
# Also shows how to right justify a string.

N = 10  # times table goes 1 to N-1

max_value = (N - 1) * (N - 1)           # max value computed
field_width = 1 + len(str(max_value))   # field width for right justifying

for row in range(1, N):
    for column in range(1, N):
        print(str(row * column).rjust(field_width), end = '')

    print("")
