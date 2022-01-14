def fahrenheit_to_celsius(tempf):
    return (tempf - 32) * 5 / 9     # note: floating division

temperatures = [14, -4, 23, 5, 41, -22]

index = 0
while index < len(temperatures):
    temperatures[index] = fahrenheit_to_celsius(temperatures[index])
    index = index + 1

print(temperatures)
