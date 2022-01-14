# clock.py
# By THC.  Counts out one number every half second.

from time import sleep

n = 1

while True:
    print(n)
    n = n + 1
    sleep(0.5)    # sleep for half a second
