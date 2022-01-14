# loan1.py
# By THC

# Finds the final balance of a loan, given the amount borrowed,
# the annual interest rate, the number of monthly payments,
# and the amount of each monthly payment.

# Return the balance left on a loan, given the principal,
# annual interest rate, the number of months of the loan,
# and the monthly payment.
def amortize(principal, rate, months, payment):
    balance = principal     # the balance remaining

    # The rate is given as a yearly percentage, but it needs
    # to be a monthly fraction.  Divide by 100 to convert to
    # a fraction and by 12 to get a monthly rate.
    rate /= (100 * 12)

    # Now simulate what happens each month.
    for month in range(months):
        balance += (rate * balance) - payment

    return balance

# Test out the amortize function.
params = input("Enter principal, rate, months, payment: ")
params = params.strip().split(' ')
principal = float(params[0])
rate = float(params[1])
months = int(params[2])
payment = float(params[3])

balance = amortize(principal, rate, months, payment)
print("After " + str(months) + " months, the final balance is $" + str(round(balance, 2)))
