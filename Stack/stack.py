class Stack(object):
    """
    A simple implementation of a stack data structure.

    Attributes:
        stack (list): A list to store elements in the stack.

    Methods:
        __init__(): Initializes an empty stack.
        push(key): Adds the specified key to the top of the stack.
        pop(): Removes and returns the element from the top of the stack.
        top(): Returns the element at the top of the stack without removing it.
        isEmpty(): Checks if the stack is empty.
        size(): Returns the number of elements in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.

        Example:
        >>> my_stack = Stack()
        """
        self.stack = []

    def __repr__(self):
        """
        Returns a string representation of the stack.

        Returns:
            str: A space-separated string representation of the elements in the stack.

        Example:
        >>> my_stack = Stack()
        >>> my_stack.push(1)
        >>> my_stack.push(2)
        >>> my_stack.push(3)
        >>> print(repr(my_stack))
        '1 2 3'
        """
        return " ".join(map(str, self.stack))

    def push(self, key):
        """
        Adds the specified key to the top of the stack.

        Args:
            key: The element to be added to the stack.

        Example:
        >>> my_stack.push(42)
        """
        self.stack.append(key)

    def pop(self):
        """
        Removes and returns the element from the top of the stack.

        Returns:
            The element removed from the top of the stack.

        Raises:
            Exception: If the stack is empty.

        Example:
        >>> popped_element = my_stack.pop()
        """
        if not self.isEmpty():
            return self.stack.pop(-1)
        raise Exception("Stack is empty")

    def top(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            The element at the top of the stack.

        Raises:
            Exception: If the stack is empty.

        Example:
        >>> top_element = my_stack.top()
        """
        if not self.isEmpty():
            return self.stack[-1]
        raise Exception("Stack is empty")

    def isEmpty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.

        Example:
        >>> is_empty = my_stack.isEmpty()
        """
        if self.stack:
            return False
        return True

    def size(self):
        """
        Returns the number of elements in the stack.

        Returns:
            The number of elements in the stack.

        Example:
        >>> stack_size = my_stack.size()
        """
        return len(self.stack)