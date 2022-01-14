the_list = [89, 83, 85, 81, 77, 94, 22, 79, 92, 91]
print("grade_list before sorting: ", the_list)

# Selection sort algorithm pseudo-code:
#   for each consecutive index i in the list:
#     find the minimum value in the sublist starting at index i.
#     call the index of this value smallest.  
#     swap the items at indices i and smallest.

def selection_sort(the_list):
    n = len(the_list)     # makes it easy to denote the length of the list

    for i in range(n - 1):
        # Uncomment the next line to see the list at the start of this iteration.
        # print("the list before iteration for i =", i, "is", the_list)

        # Find the minimum value in the sublist starting at index i.
        # smallest will hold the index of the smallest value we have found
        # so far in the sublist.
        smallest = i

        for j in range(i, n):
            if the_list[j] < the_list[smallest]:
                smallest = j

        # After the inner loop, smallest has the index of the smallest
        # value in the sublist starting at index i.  Swap the values
        # at index i and smallest.
        the_list[i], the_list[smallest] = the_list[smallest], the_list[i]

selection_sort(the_list)
print("grade_list after sorting:  ", the_list)
