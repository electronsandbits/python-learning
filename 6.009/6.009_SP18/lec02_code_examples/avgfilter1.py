## Program number 1
input_list = [100, 27, 93, 94, 107, 10]

averaged_result = [0] * 4

averaged_result[0] = (input_list[0] + input_list[1] + input_list[2]) / 3
averaged_result[1] = (input_list[1] + input_list[2] + input_list[3]) / 3
averaged_result[2] = (input_list[2] + input_list[3] + input_list[3]) / 3
averaged_result[1] = (input_list[3] + input_list[4] + input_list[5]) / 3

print(averaged_result)
