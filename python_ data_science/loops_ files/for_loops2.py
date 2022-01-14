app_ratings = [3.5, 4.5, 4.5, 4.5, 4.5]

for element in app_ratings:
    print(element)


app_names = ['Facebook', 'Instagram', 'Clash of Clans', 'Fruit Ninja Classic', 'Minecraft: Pocket Edition']
for name in app_names:
    print(name)


row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

for row in app_data_set:
    rating = row[-1]
    print(rating)



a_list = [1, 3, 5]

a_sum = 0
for value in a_list:
    a_sum = a_sum + value
    print(a_sum)

print(a_sum)




row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0

for row in  app_data_set:
    rating_count = row[3]
    rating_sum += rating_count
print(rating_sum)


row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0
for row in app_data_set:
    rating = row[-1]
    rating_sum += rating

avg_rating = rating_sum / 5
print(avg_rating)
