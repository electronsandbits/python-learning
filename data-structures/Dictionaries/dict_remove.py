"""
Removing an Entry
"""
cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print(cities)
cities.popitem() # Deletes 'Ireland' entry
print(cities)
cities.pop('Northern Ireland')
print(cities)
del cities['Scotland']
print(cities)