# map operator names to appropriate arithmetic function
otable = {
    '+': (lambda x,y: x + y),
    '-': (lambda x,y: x - y),
    '*': (lambda x,y: x * y),
    '/': (lambda x,y: x / y),
}

def eval_ast(ast, env={}):
    """
    Evaluate the given AST in the given environment.

    ast is one of the following forms:
        * a single number
        * a string representing a variable name
        * a list [operation, operand, operand, operand, ...]
            where operation is a key in the operators dictionary
            and the operands are themselves ast's

    env is a dictionary mapping variable names to values
    """
    raise NotImplementedError


def tokenize(exp):
    """
    Split an expression into meaningful tokens.
    exp is a fully-parenthesized infix math expression.

    For example:
    ((x + 2) * 3) => ['(', '(', 'x', '+', '2', ')', '*', '3', ')']
    """
    raise NotImplementedError


def parse(tokens):
    """
    Convert a list of tokens (like that returned by tokenize) into an
    ast (like that expected by eval_ast)

    Example:
    ['(', 'x', '+', '(', '2', '+', '3', ')', ')']  =>  ['+', 'x', ['+', 2, 3]]
    """
    raise NotImplementedError
