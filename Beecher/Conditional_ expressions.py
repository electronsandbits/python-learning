"""
Conditional expressions:[value if true] if [condition] else [value if false]: max = a if a > b else b
"""
if a > b:
    # a is higher than b, therefore it’s the maximum.
    max = a

else:
    # Return b, either because it’s higher than a, or
    # because a and b are the same.
    max = b
