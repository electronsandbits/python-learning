"""
Evaluating a postfix expression is easier than evaluating an infix expression because
it does not contain any parentheses and there are no operator precedence rules to
consider. A postfix expression can be evaluated using the following algorithm:
Create a new empty list, values
For each token in the postfix expression
  If the token is a number then
     Convert it to an integer and append it to values
  Else if the token is a unary minus then
     Remove an item from the end of values
     Negate the item and append the result of the negation to values
  Else if the token is a binary operator then
     Remove an item from the end of values and call it right
     Remove an item from the end of values and call it left
     Compute the result of applying the operator to left and right
     Append the result to values
  Return the first item in values as the value of the expression

 Write a program that reads a mathematical expression in infix form from the user,
converts it to postfix form, evaluates it, and displays its value. Use your solutions
to Exercises 129, 130 and 131, along with the algorithm shown above, to solve this
problem.



The algorithms provided in Exercises 131 and 132 do not perform any error
checking. As a result, your programs may crash or generate incorrect results if
you provide them with invalid input. The algorithms presented in these exercises
can be extended to detect invalid input and respond to it in a reasonable
manner. Doing so is left as an independent study exercise for the interested
student.
"""