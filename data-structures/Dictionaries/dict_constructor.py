"""
The dict() Constructor Function
"""
# note keys are not strings
dict1 = dict(uk='London', ireland='Dublin', france='Paris')
print('dict1:', dict1)

# key value pairs are tuples
dict2 = dict([('uk', 'London'), ('ireland', 'Dublin'),('france', 'Paris')])
print('dict2:', dict2)

# key value pairs are lists
dict3 = dict((['uk', 'London'], ['ireland', 'Dublin'], ['france', 'Paris']))
print('dict3:', dict3)