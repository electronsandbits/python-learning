#
# File: binary_search.py
# ----------------------------
# The binary_search function  takes a sorted array and an item.
# If the item is in the array, the function returns its position.
#

def  binary_search( list ,  item):
     low = 0
     high = len (list)  - 1

     while  low <= high :             # While you haven't narrowed it down to one element
        mid  =  (low + high)       # Check the middle element    
        guess = list [mid]
        if  guess  == item :        # Found the item
           return mid
        if  guess > item :           # The guess was too high
           high = mid - 1
        else:                                # The guess was too low
           low  = mid + 1
     return None                          # The item doesn't exist
my_list = [ 1 ,3, 5, 7, 9 ]

print binary_search(my_list, 3)
print binary_search(my_list, -1)
               
                
                 
