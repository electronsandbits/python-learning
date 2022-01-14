# CS1:Fall 2019
# Lecture 7: List and for-loops
# Iterating over a list with a while loop

def fahrenheit_to_celsius(tempf):
    return (tempf - 32) * 5 / 9  # note: floating division

temperatures = [14, -4, 23, 5, 41, -22]

temperatures[0] = fahrenheit_to_celsius(temperatures[0])
temperatures[1] = fahrenheit_to_celsius(temperatures[1])
temperatures[2] = fahrenheit_to_celsius(temperatures[2])
temperatures[3] = fahrenheit_to_celsius(temperatures[3])
temperatures[4] = fahrenheit_to_celsius(temperatures[4])
temperatures[5] = fahrenheit_to_celsius(temperatures[5])


print(temperatures)
