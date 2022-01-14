## Program number 2 (combine logically-equivalent lines into one loop)
input_list = [100, 27, 93, 94, 107, 10]

averaged_result = []
for i in range(2, 6):
    this_avg = (input_list[i - 2] + input_list[i - 1] + input_list[i]) / 3
    averaged_result.append(this_avg)

print(averaged_result)
