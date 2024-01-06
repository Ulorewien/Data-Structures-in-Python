class Node(object):
    """
    A simple implementation of a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list.

    Methods:
        __init__(data=0): Initializes a node with the given data.
        __repr__(): Returns a string representation of the node.
    """

    def __init__(self, data = 0, double = False):
        """
        Initializes a node with the given data.

        Args:
            data: The data to be stored in the node.
            double (bool): If True, creates a doubly linked list node with a 'prev' reference.

        Example:
        >>> node = Node(42)
        >>> doubly_linked_node = Node(42, double=True)
        """
        self.data = data
        self.next = None
        if double:
            self.prev = None

    def __repr__(self):
        """
        Returns a string representation of the node.

        Returns:
            str: The string representation of the node.

        Example:
        >>> node = Node(42)
        >>> print(repr(node))
        '42'
        """
        return str(self.data)