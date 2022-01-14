# List reverse example for cs1
# Devin Balkcom
# August 2011
# Minor changes by THC.

# An example list
my_list = [1, 3, 5, 7, 9, 11, 13, 15]

print("The list before reversing:  " + str(my_list))

left_index = 0  # index of the left item of the pair to swap
while left_index < len(my_list) // 2:
    # Because indices start at 0, the last item of the list is at 
    # index len(l) - 1.
    right_index = len(my_list) - 1 - left_index     # index of right item of the pair

    # Swap the items at left_index and right_index.
    my_list[left_index], my_list[right_index] = my_list[right_index], my_list[left_index]

    left_index = left_index + 1
    
print("The list after reversing:  " + str(my_list))
