## Program number 5 (generalize to arbitrary k)
def averaging_filter(inputs, k):
    result = []
    for i in range(k-1, len(inputs)):
        total = 0.0
        for index in range(i-k+1, i+1):
            total = total + inputs[index]
        result.append(total / k)
    return result

print(averaging_filter([100, 27, 93, 94, 107, 10], 3))

print(averaging_filter([94, 38, 96, 20, 18, 100, 108], 3))
