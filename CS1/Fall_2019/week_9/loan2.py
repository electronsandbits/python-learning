# loan2.py
# By THC

# Finds the monthly payment for a loan, given the amount borrowed,
# the annual interest rate, and the number of monthly payments.
# Works by finding a monthly payment such that if we use that monthly
# payment, the balance after all the months is close to zero.
# We find this monthly payment by starting at a small payment, where
# that balance is positive, and doubling it until the balance becomes
# negative.  The payment we're looking for is between the last two balances
# tried.  We then bisect this interval until we get payments within one cent
# with one having a nonpositive balance and one having a positive balance.
# We choose the payment with the nonpositive balance.

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

# Find two monthly payments such that one gives a positive balance and
# the other gives a negative balance.  Return a tuple with these two payments.
def bracket_payment(principal, rate, months):
    # Assuming that rate > 0, we know that a payment of principal / months
    # will yield a positive balance.  Start with an interval where
    # left = principal / months (guaranteed to be too low a payment) and
    # right = 2 * principal / months (don't know if it's too high a payment).
    left = principal / months
    right = 2 * left

    # As long as the right end is too low a payment (balance after running
    # amortize is positive), keep doubling it.  Before doubling it, we can
    # set left to the right end that we know is too small, which is a nice,
    # simple optimization.
    while amortize(principal, rate, months, right) > 0:
        left = right
        right *= 2

    # At this point, the balance or left is positive and the balance for right
    # is nonpositive, so we're done.
    return (left, right)

# Bisect an interval of monthly payments to find, to the penny, the balance
# that is nonpositive and closest to zero.
# Maintains the invariant that left is a payment that is too low and right
# is a payment that is too high.
def find_payment(principal, rate, months, left, right):
    PENNY = 0.01

    while right - left >= PENNY:
        midpoint = (left + right) / 2
        balance = amortize(principal, rate, months, midpoint)

        # If the balance is positive, then midpoint still isn't enough payment.
        # If the balance is negative, then midpoint is too much payment.
        if balance > 0:
            left = midpoint
        else:
            right = midpoint

    # At this point, we have the interval down to less than one cent.
    # We should always return a value that gives a nonpositive balance, so
    # that we have not underpaid.  Since we want a value that is correct to the
    # penny, we convert the right end of the interval from dollars to pennies,
    # take the ceiling (smallest integer greater than or equal), and convert back
    # to pennies.
    return PENNY * ceil(right / PENNY)

# Test out finding the payment.
params = input("Enter principal, rate, months: ")
params = params.strip().split(' ')
principal = float(params[0])
rate = float(params[1])
months = int(params[2])

(left, right) = bracket_payment(principal, rate, months)
payment = find_payment(principal, rate, months, left, right)
print("The monthly payment is $" + str(round(payment, 2)))
