def reverse_list(l):
    index = 0
    while index < len(l) // 2:
        # We'll call the index of the item to swap with the right_index,
        # since it's the index into the right half of the list.
        # Because indices start at 0, the last item of the list is at
        # index len(l) - 1.
        right_index = len(l) - 1 - index
    
        # Swap the items at index and right_index.
        l[index], l[right_index] = l[right_index], l[index]
    
        index = index + 1
    
test_list = [1, 3, 5, 7, 9, 11, 13, 15]
print("The list before reversing:  " + str(test_list))
reverse_list(test_list)
print("The list after reversing:  " + str(test_list))

test_list = [1, 3, 5, 7, 9, 11, 13, 15]
rlist = list(test_list)
reverse_list(rlist)
print("Reversed:  " + str(rlist))
print("Not reversed:  " + str(test_list))
