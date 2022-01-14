# a simple example of a list that
# contains a few kinds of bicycles:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

# This code returns the second and fourth bicycles in the list
print(bicycles[1].title())
print(bicycles[3].title())

# Prints the last item in the list
print(bicycles[-1])

# Using individual values from a list
message =f"My first bicycle was a {bicycles[0].title()}."
print(message)
