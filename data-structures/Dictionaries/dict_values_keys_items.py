"""
Values, Keys and Items
- The values() method returns a view onto the dictionary’s values.
- The keys() method returns a view onto a dictionary’s keys.
- The items() method returns a view onto the dictionary’s items ((key, value) pairs).
"""

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print(cities.values())
print(cities.keys())
print(cities.items())



