



row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

data_set = [row_1, row_2, row_3, row_4, row_5]

print(data_set[0]) # Retrieve the first list element (row_1) using data_set[0]
print(data_set[-1]) # Retrieve the last list element (row_5) using data_set[-1]
print(data_set[:2]) # Retrieve the first two list ele (row_1 and row_2) by performing list slicing using data_set[:2]


"""
In the code editor, we've already stored the five rows as lists in separate variables. Group the five lists together in a list of lists. Assign the resulting list of lists to a variable named app_data_set.
Calculate the average rating of the apps by retrieving the right data points from the app_data_set list of lists.
The rating is the last element of each row. You'll need to add up the ratings and then divide by the number of rows.
Assign the result to a variable named avg_rating.
"""
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

total = row_1[-1] + row_2[-1] + row_3[-1] + row_4[-1] + row_5[-1]
print(total)

avg_rating = total / 5
print(avg_rating)
