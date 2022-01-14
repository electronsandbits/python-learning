"""
The following statements
read a customer’s name, the quantity of an item that they would like to purchase, and
the item’s price
"""
name = input("Enter your name: ")
quantity = int(input("How many items? "))
price = float(input("Cost per item ? "))

total = quantity * price
print("total = quantity * price")