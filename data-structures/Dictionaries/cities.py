cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print(cities)

# Accessing Items via Keys
print('cities[Wales]:', cities['Wales'])
print('cities.get(Ireland):', cities.get('Ireland'))


# Adding a New Entry
cities['France'] = 'Paris'
cities['Germany'] = 'Berlin'

# Changing a Keys Value
cities['Wales'] = 'Swansea'
print(cities)


