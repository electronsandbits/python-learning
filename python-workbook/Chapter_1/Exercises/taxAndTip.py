"""
Exercise 6: Tax and Tip

The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.

file:TaxAndTip.py
-----------------
This program reads the cost of a meal ordered at a restaurant from the user.
Then program will compute the tax and tip for the meal.

@author:electronsandbits
@version:December 9, 2021
"""

# Constants
# Compute the tax and tip for a restaurant meal.
TAX_RATE = 0.05
TIP_RATE = 0.18

# Reads the cost of a meal from the user
cost_of_meal = float(input("Enter the cost of the meal: "))

# Compute the tax, and tip, for the meal
tax_amount = cost_of_meal * TAX_RATE
tip_amount = cost_of_meal * TIP_RATE

# Compute the grand total
total = tip_amount + tip_amount + cost_of_meal

# Display the total
print("The tax is %.2f and the tip is %.2f, making the", "total %.2f" % (tax_amount, tip_amount, total))
