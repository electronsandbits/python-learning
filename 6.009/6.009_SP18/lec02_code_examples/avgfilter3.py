## Program number 3 (but what if we want to compute for multiple lists?)
input_list = [100, 27, 93, 94, 107, 10]

averaged_result = []
for i in range(2, 6):
    this_avg = (input_list[i - 2] + input_list[i - 1] + input_list[i]) / 3
    averaged_result.append(this_avg)

print(averaged_result)

input_list2 = [94, 38, 96, 20, 18, 100, 108]

averaged_result2 = []
for i in range(2, 7):
    this_avg = (input_list[i - 2] + input_list[i - 1] + input_list[i]) / 3
    averaged_result.append(this_avg)

print(averaged_result2)
