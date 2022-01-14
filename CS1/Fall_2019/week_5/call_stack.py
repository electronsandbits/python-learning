def functionA():
    print("A called.")
    x = 5
    functionC()
    print("In A, x =", x)
    
def functionB():
    y = 10
    print("B called.")
    
def functionC():
    x = 2
    k = 6
    print("C called.")
    functionB()
    functionD()
    print("In C, x =", x)
    
def functionD():
    z = 12
    print("D called.")

functionA()
