from node import Node
    
class CircularLinkedList(object):
    """
    A simple implementation of a circular linked list.

    Attributes:
        head: Reference to the first node in the circular linked list.

    Methods:
        __init__(): Initializes an empty circular linked list.
        __repr__(): Returns a string representation of the circular linked list.
        insertAtBegin(data): Inserts a node with the given data at the beginning of the circular linked list.
        insertAtIndex(data, index): Inserts a node with the given data at the specified index in the circular linked list.
        insertAtEnd(data): Inserts a node with the given data at the end of the circular linked list.
        updateNode(data, index): Updates the data of the node at the specified index in the circular linked list.
        removeFirstNode(): Removes the first node from the circular linked list.
        removeNodeAtIndex(index): Removes the node at the specified index from the circular linked list.
        removeLastNode(): Removes the last node from the circular linked list.
        length(): Returns the length of the circular linked list.
    """

    def __init__(self):
        """
        Initializes an empty circular linked list.

        Example:
        >>> my_circular_list = CircularLinkedList()
        """
        self.head = None

    def __repr__(self):
        """
        Returns a string representation of the circular linked list.

        Returns:
            str: The string representation of the circular linked list.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtEnd(1)
        >>> my_circular_list.insertAtEnd(2)
        >>> my_circular_list.insertAtEnd(3)
        >>> print(repr(my_circular_list))
        '1 -> 2 -> 3 -> 1'
        """
        if not self.head:
            return "List is Empty!"
        node = self.head
        res = []
        while node.next != self.head:
            res.append(node.data)
            node = node.next
        res.append(node)
        res.append(node.next)
        return " -> ".join(map(str, res))

    def insertAtBegin(self, data):
        """
        Inserts a node with the given data at the beginning of the circular linked list.

        Args:
            data: The data to be stored in the new node.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtBegin(42)
        """
        if self.head:
            newNode = Node(data)
            newNode.next = self.head
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = newNode
            self.head = newNode
        else:
            self.head = Node(data)
            self.head.next = self.head

    def insertAtIndex(self, data, index):
        """
        Inserts a node with the given data at the specified index in the circular linked list.

        Args:
            data: The data to be stored in the new node.
            index (int): The index at which the new node should be inserted.

        Raises:
            AssertionError: If the index is not an integer.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtEnd(1)
        >>> my_circular_list.insertAtEnd(3)
        >>> my_circular_list.insertAtIndex(2, 1)
        """
        assert isinstance(index, int)

        l = self.length()
        if index > l or index < 0:
            print("Invalid Index")
        elif index == 0:
            self.insertAtBegin(data)
        elif index == l:
            self.insertAtEnd(data)
        else:
            current = self.head
            ct = 1
            while ct < index:
                current = current.next
                ct += 1
            newNode = Node(data)
            newNode.next = current.next
            current.next = newNode

    def insertAtEnd(self, data):
        """
        Inserts a node with the given data at the end of the circular linked list.

        Args:
            data: The data to be stored in the new node.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtEnd(42)
        """
        if self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            newNode = Node(data)
            current.next = newNode
            newNode.next = self.head
        else:
            self.head = Node(data)
            self.head.next = self.head

    def updateNode(self, data, index):
        """
        Updates the data of the node at the specified index in the circular linked list.

        Args:
            data: The new data to be stored in the node.
            index (int): The index of the node to be updated.

        Raises:
            AssertionError: If the index is not an integer.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtEnd(1)
        >>> my_circular_list.insertAtEnd(2)
        >>> my_circular_list.insertAtEnd(3)
        >>> my_circular_list.updateNode(42, 1)
        """
        assert isinstance(index, int)

        l = self.length()
        if index > l or index < 0:
            print("Invalid Index")
        else:
            ct = 0
            current = self.head
            while ct < index:
                current = current.next
                ct += 1
            current.data = data

    def removeFirstNode(self):
        """
        Removes the first node from the circular linked list.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtEnd(1)
        >>> my_circular_list.removeFirstNode()
        """
        if self.head:
            if self.head.next == self.head:
                del self.head
                self.head = None
            else:
                current = self.head.next
                last = current
                while last.next != self.head:
                    last = last.next
                del self.head
                self.head = current
                last.next = self.head
        else:
            print("List is Empty!")

    def removeNodeAtIndex(self, index):
        """
        Removes the node at the specified index from the circular linked list.

        Args:
            index (int): The index of the node to be removed.

        Raises:
            AssertionError: If the index is not an integer.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtEnd(1)
        >>> my_circular_list.insertAtEnd(2)
        >>> my_circular_list.insertAtEnd(3)
        >>> my_circular_list.removeNodeAtIndex(1)
        """
        assert isinstance(index, int)

        l = self.length()
        if l == 0:
            print("List is Empty!")
        elif index >= l or index < 0:
            print("Invalid Index")
        elif index == 0:
            self.removeFirstNode()
        elif index == l-1:
            self.removeLastNode()
        else:
            ct = 1
            current = self.head
            while ct < index:
                current = current.next
                ct += 1
            temp = current.next.next
            del current.next
            current.next = temp

    def removeLastNode(self):
        """
        Removes the last node from the circular linked list.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtEnd(1)
        >>> my_circular_list.insertAtEnd(2)
        >>> my_circular_list.removeLastNode()
        """
        if not self.head:
            print("List is Empty!")
        elif self.head.next == self.head:
            self.removeFirstNode()
        else:
            prev = self.head
            current = prev.next
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = self.head
            del current

    def length(self):
        """
        Returns the length of the circular linked list.

        Returns:
            int: The length of the circular linked list.

        Example:
        >>> my_circular_list = CircularLinkedList()
        >>> my_circular_list.insertAtEnd(1)
        >>> my_circular_list.insertAtEnd(2)
        >>> my_circular_list.insertAtEnd(3)
        >>> my_circular_list.length()
        3
        """
        if not self.head:
            return 0
        ct = 1
        current = self.head
        while current.next != self.head:
            ct += 1
            current = current.next
        return ct