## Program number 4 (define a function!  accepts list of arbitrary length)
def averaging_filter(inputs):
    result = []
    for i in range(2, len(inputs)):
        avg_val = (inputs[i - 2] + inputs[i - 1] + inputs[i]) / 3
        result.append(avg_val)
    return result

print(averaging_filter([100, 27, 93, 94, 107, 10]))
print(averaging_filter([94, 38, 96, 20, 18, 100, 108]))
