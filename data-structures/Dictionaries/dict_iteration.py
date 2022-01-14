"""
Iterating over Keys
"""
cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
for country in cities:
    print(country, end=', ')
    print(cities[country])