"""
Mathematical expressions are often written in infix form, where operators appear
between the operands on which they act. While this is a common form, it is also
possible to express mathematical expressions in postfix form, where the operator
appears after all of its operands. For example, the infix expression3 + 4is written
as3 4 +in postfix form. One can convert an infix expression to postfix form using
the following algorithm:
Create a new empty list, operators
Create a new empty list, postfix

For each token in the infix expression
  If the token is an integer then
     Append the token to postfix
  If the token is an operator then
     While operators is not empty and
           the last item in operators is not an open parenthesis and
           precedence(token) < precedence(last item in operators) do
        Remove the last item from operators and append it to postfix
     Append the token to operators

  If the token is an open parenthesis then
     Append the token to operators
  If the token is a close parenthesis then
     While the last item in operators is not an open parenthesis do
         Remove the last item from operators and append it to postfix
     Remove the open parenthesis from operators
While operators is not the empty list do
   Remove the last item from operators and append it to postfix
   
Return postfix as the result of the algorithm
"""