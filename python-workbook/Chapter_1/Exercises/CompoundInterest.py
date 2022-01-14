"""
file: CompoundInterest.py
-------------------------
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account.

Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places.
------------------------------------------------------------------------------------------------------------
                                   Compound Interest
                                   A(t) = P(1 + r * n)** n * t

    where            A(t)=  amount after t years
                     P  =  principal
                     r = interest rate per year
                     n = number of times interest is compounded per year
                     t = number of years

def compound_interest(principle, rate, time)

 -----------------------------
 Compounding                n
 -----------------------------
    Annual                  1
    Semiannual              2
    Quarterly               4
    Monthly                12
    Daily                  365

@author: @electronsandbits
@version: December 13, 2021

"""

# r = 0.04
# 2 decimal places: $%.2f.

# Define the constants
rate = 12 / 100

# prompt the user to enter the initial amount
principal = float(input("Enter the amount:  $"))
n = int(input("Enter the number of times interest is compounded per year:  "))
t = int(input("Enter the number os years: "))

# Calculate the amount
amount = principal * pow(1 + (rate/n), n * t)


compound_interest = amount - principal

# Display the amount
print('Compound interest = %.2f' % compound_interest)
print('Total amount = %.2f' % amount)


