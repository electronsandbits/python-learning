"""
File:MonthNameToNumberOfDays.py
-------------------------------
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.

@author: @electronsandbits
@version: December 14, 2021
"""

month = input("Enter the name of a month:  ")

if month == "April" or month == "June" or month == "September" or month == "November":
    print("30 days")
elif month == "February":
    print("28 or 29 days")
else:
    print("31 days")

