from stack import Stack

def precedence(operator):
    """
    Determines the precedence of an operator.

    Args:
        operator (str): The operator to check. Should be one of "^", "*", "/", "+", "-", "(".

    Returns:
        int: The precedence value for the operator. Higher values indicate higher precedence.

    Raises:
        AssertionError: If the input operator is not one of the specified operators.

    Example:
    >>> precedence("^")
    3
    """
    assert operator in ["^", "*", "/", "+", "-", "("]

    if operator == "^":
        return 3
    elif operator in ["*", "/"]:
        return 2
    elif operator in ["+", "-"]:
        return 1
    return -1
    
def infixToPostfix(eq):
    """
    Converts an infix expression to postfix notation.

    Args:
        eq (str): The infix expression to be converted.

    Returns:
        str: The postfix expression.

    Raises:
        AssertionError: If the input is not a string.

    Example:
    >>> infixToPostfix("a + b * c")
    'a b c * +'
    """
    assert isinstance(eq, str)

    eq = eq.replace(" ","")
    res = ""
    s = Stack()

    for c in eq:
        if c in ["^", "*", "/", "+", "-"]:
            p = precedence(c)
            while (not s.isEmpty()) and (precedence(s.top()) >= p):
                res += s.pop()
            s.push(c)
        elif c == "(":
            s.push(c)
        elif c == ")":
            while s.top() != "(":
                res += s.pop()
            s.pop()
        else:
            res += c
    
    while (not s.isEmpty()):
        res += s.pop()

    if not res:
        return "No equation"
    return res

print(infixToPostfix("a+b*c+d"))
print(infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))
print(infixToPostfix("((A + B) - C * (D / E)) + F"))
print(infixToPostfix("((A + (B * C)) + D)"))
print(infixToPostfix("A + B * C"))
print(infixToPostfix(""))
print(infixToPostfix(" "))
print(infixToPostfix("a^(b+c)"))