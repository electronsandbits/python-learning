# merge_sort.py
# Merge sort example for cs1
# Devin Balkcom
# October, 2011
# Modified by THC.

# Take two sorted lists, the_list[p ... q] and the_list[q+1 ... r],
# and merge them into the_list[p ... r].
def merge(the_list, p, q, r):
    # Make a copy of the list items.  OK to use slicing here to copy.
    left = the_list[p : q+1]
    right = the_list[q+1 : r+1]
 
    # Until we've gone through one of left and right, move
    # the smallest unmerged item into the next position in
    # the_list[p ... r].
    
    i = 0       # index into left
    j = 0       # index into right
    k = p       # index into the_list[p ... r]
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            the_list[k] = left[i]
            i += 1
        else:
            the_list[k] = right[j]
            j += 1
        k += 1
    
    # We've gone through one of left and right entirely.
    # Copy the remainder of the other to the end of the_list[p ... r].
    
    # If left has remaining items, copy them into the_list, using list slices.
    if i < len(left):
        the_list[k : r+1] = left[i:]
    
    # If right has remaining items, copy them into the_list, using list slices.
    if j < len(right):
        the_list[k : r+1] = right[j:]
        
# Sort the_list[p ... r], using merge sort.
def merge_sort(the_list, p = 0, r = None):
    # If using the default parameters, sort the entire list.
    if r == None:
        r = len(the_list) - 1

    if p < r:   # nothing to do if the sublist has fewer than 2 items
        q = (p + r) // 2                # midpoint of p and r
        merge_sort(the_list, p, q)      # recursively sort the_list[p ... q]
        merge_sort(the_list, q+1, r)    # recursively sort the_list[q+1 ... r]
        merge(the_list, p, q, r)        # and merge them together

if __name__ == '__main__':
    grade_list = [89, 83, 85, 81, 77, 94, 22, 79, 92, 91]
    print("grade_list before sorting: ", grade_list)
    merge_sort(grade_list)
    print("grade_list after sorting:  ", grade_list)
