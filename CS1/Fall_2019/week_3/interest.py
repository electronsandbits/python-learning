RATE = 5    # percent
YEAR = 2019
balance = 1.0

for year in range(0, YEAR):
    balance = balance * (1 + (RATE / 100))

print("The balance is " + str(balance) + ".")
