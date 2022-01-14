# loan3.py
# By THC

# Finds the monthly payment for a loan, given the amount borrowed,
# the annual interest rate, and the number of monthly payments.
# Works by stupidly starting the payment at $0.01 and increasing the
# payment by $0.01 at a time, until the balance due after running the
# loan is zero or negative.

from math import ceil

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

# Starting at a penny and increasing by a penny each time, find the
# first payment that yields a nonpositive balance.
def slow_find_payment(principal, rate, months):
    PENNY = 0.01
    payment = PENNY

    while amortize(principal, rate, months, payment) > 0:
        payment += PENNY

    # Because of floating-point imprecision, make sure to round up
    # the payment to the next penny.
    return PENNY * ceil(payment / PENNY)

# Test out finding the payment.
params = input("Enter principal, rate, months: ")
params = params.strip().split(' ')
principal = float(params[0])
rate = float(params[1])
months = int(params[2])

payment = slow_find_payment(principal, rate, months)
print("The monthly payment is $" + str(round(payment, 2)))
