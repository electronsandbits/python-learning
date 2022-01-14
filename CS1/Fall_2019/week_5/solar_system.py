# solar_system.py
# Shows how to sort objects using methods.

from planet import Planet
from merge_sort import merge_sort
from insertion_sort import insertion_sort

planets = [Planet('Mercury', 3.3e23), Planet('Venus', 4.87e24), Planet('Earth', 5.97e24),
           Planet('Mars', 6.43e23), Planet('Jupiter', 1.898e27), Planet('Saturn', 5.68e26),
           Planet('Uranus', 8.68e25), Planet('Neptune', 1.02e26), Planet('Pluto', 1.45e22)]

print("Unsorted:")
for body in planets:
    print(body)

Planet.__lt__ = Planet.mass_lt
merge_sort(planets)

print("\nSorted by mass:")
for body in planets:
    print(body)

Planet.__gt__ = Planet.name_gt
insertion_sort(planets)

print("\nSorted by name:")
for body in planets:
    print(body)
