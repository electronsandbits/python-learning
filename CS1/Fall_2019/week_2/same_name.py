x = 5   # global variable

def something():
    x = 8       # local variable
    print(x)    # refers to the local variable

def other():
    print(x)    # refers to the global variable

something()
other()
print(x)        # refers to the global variable
