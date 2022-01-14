"""
file:geometric_serie.py
-----------------------
The following program demonstrates the sumGeometric function by computing
sums until the user enters zero for a. Each sum is computed inside the function
and then returned to the location where the function was called. Then the returned
value is stored in the total variable using an assignment statement. A subsequent
statement displays total before the program goes on and reads the values for
another sequence from the user

"""

def geometric_serie():
    # Read the initial value for the first sequence
    initial_value = float(input("Enter the value of a (0 to quit): "))

    # While the initial value is non-zero
    while initial_value != 0:
        # Read the ratio and number of terms
        ratio = float(input("Enter the ratio, r: "))
        number = int(input("Enter the number of terms, n:  "))

        # Compute and display the total
        total = geometric_serie(initial_value, ratio, number)
        print("The sum of the first ", number, "terms is", total)

        # Read the initial value for the next sequence
        initial_value = float(input("Enter the value of a (0 to quit): "))

# Call the function
geometric_serie()