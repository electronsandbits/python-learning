def insertion_sort(L):
    if len(L) == 0:
        return []  # base case
    else:
        this_elt = L[0]
        sorted_rest = insertion_sort(L[1:])
        for ix in range(len(sorted_rest)):
            if sorted_rest[ix] > this_elt:
                return sorted_rest[:ix] + [this_elt] + sorted_rest[ix:]
        return sorted_rest + [this_elt]

###############################

def merge_sort(L):
    """Returns a new sorted list containing the
    same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(L1, L2):
    result = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    result.extend(L1[i:])
    result.extend(L2[j:])
    return result

