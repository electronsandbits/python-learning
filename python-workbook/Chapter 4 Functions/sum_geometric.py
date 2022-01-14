"""
sum_geometric.py
----------------
This program computes the sum of the first n terms of any
geometric sequence. It will require 3 parameters: a, r and n, and it will need to
return one result, which is the sum of the first n terms.
===============================
sum = a(1 - r **n) / (1 - r)
===============================
Compute the sum of the first n terms of a geometric sequence.
@param a the first term in the sequence
@param r the common ratio for the sequence
@param n the number of terms to include in the sum
@return the sum of the first n term of the sequence

"""

def sum_geometric(a, r, n):
    """
     Compute and return the sum when the common ratio is 1
    """
    if r == 1:
        return a * n
    # Compute and return the sum when the common ratio is not 1
    sum = a * (1 - r ** r) / (1 - r)
    return sum


