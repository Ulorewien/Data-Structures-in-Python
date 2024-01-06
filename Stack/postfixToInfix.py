from stack import Stack

def postfixToInfix(eq):
    """
    Converts a postfix expression to infix notation.

    Args:
        eq (str): The postfix expression to be converted.

    Returns:
        str: The infix expression.

    Raises:
        AssertionError: If the input is not a string.

    Example:
    >>> postfixToInfix("abc*+")
    '((a + b) * c)'
    """
    assert isinstance(eq, str)

    res = ""
    eq = eq.replace(" ","")
    s = Stack()

    for c in eq:
        if c in ["^", "*", "/", "+", "-"]:
            a = s.pop()
            res = "(" + s.pop() + c + a + ")"
            s.push(res)
        else:
            s.push(c)

    return res

print(postfixToInfix("abc*+d+"))
print(postfixToInfix("abcd^e-fgh*+^*+i-"))
print(postfixToInfix("AB+CDE/*-F+"))
print(postfixToInfix("ABC*+D+"))
print(postfixToInfix("ABC*+"))
print(postfixToInfix("abc+^"))