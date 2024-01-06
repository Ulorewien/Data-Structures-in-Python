from node import Node
    
class LinkedList(object):
    """
    A simple implementation of a singly linked list.

    Attributes:
        head: Reference to the first node in the linked list.

    Methods:
        __init__(): Initializes an empty linked list.
        __repr__(): Returns a string representation of the linked list.
        insertAtBegin(data): Inserts a node with the given data at the beginning of the linked list.
        insertAtIndex(data, index): Inserts a node with the given data at the specified index in the linked list.
        insertAtEnd(data): Inserts a node with the given data at the end of the linked list.
        updateNode(data, index): Updates the data of the node at the specified index in the linked list.
        removeFirstNode(): Removes the first node from the linked list.
        removeNodeAtIndex(index): Removes the node at the specified index from the linked list.
        removeLastNode(): Removes the last node from the linked list.
        length(): Returns the length of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.

        Example:
        >>> my_list = LinkedList()
        """
        self.head = None

    def __repr__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtEnd(1)
        >>> my_list.insertAtEnd(2)
        >>> my_list.insertAtEnd(3)
        >>> print(repr(my_list))
        '1 -> 2 -> 3'
        """
        node = self.head
        res = []
        while node:
            res.append(node.data)
            node = node.next
        if res:
            return " -> ".join(map(str, res))
        return "List is Empty!"

    def insertAtBegin(self, data):
        """
        Inserts a node with the given data at the beginning of the linked list.

        Args:
            data: The data to be stored in the new node.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtBegin(42)
        """
        if self.head:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = Node(data)

    def insertAtIndex(self, data, index):
        """
        Inserts a node with the given data at the specified index in the linked list.

        Args:
            data: The data to be stored in the new node.
            index (int): The index at which the new node should be inserted.

        Raises:
            AssertionError: If the index is not an integer.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtEnd(1)
        >>> my_list.insertAtEnd(3)
        >>> my_list.insertAtIndex(2, 1)
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
        Inserts a node with the given data at the end of the linked list.

        Args:
            data: The data to be stored in the new node.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtEnd(42)
        """
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)

    def updateNode(self, data, index):
        """
        Updates the data of the node at the specified index in the linked list.

        Args:
            data: The new data to be stored in the node.
            index (int): The index of the node to be updated.

        Raises:
            AssertionError: If the index is not an integer.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtEnd(1)
        >>> my_list.insertAtEnd(2)
        >>> my_list.insertAtEnd(3)
        >>> my_list.updateNode(42, 1)
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
        Removes the first node from the linked list.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtEnd(1)
        >>> my_list.removeFirstNode()
        """
        if self.head:
            current = self.head.next
            del self.head
            self.head = current
        else:
            print("List is Empty!")

    def removeNodeAtIndex(self, index):
        """
        Removes the node at the specified index from the linked list.

        Args:
            index (int): The index of the node to be removed.

        Raises:
            AssertionError: If the index is not an integer.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtEnd(1)
        >>> my_list.insertAtEnd(2)
        >>> my_list.insertAtEnd(3)
        >>> my_list.removeNodeAtIndex(1)
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
        Removes the last node from the linked list.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtEnd(1)
        >>> my_list.insertAtEnd(2)
        >>> my_list.removeLastNode()
        """
        if not self.head:
            print("List is Empty!")
        elif not self.head.next:
            self.removeFirstNode()
        else:
            prev = self.head
            current = prev.next
            while current.next:
                prev = current
                current = current.next
            prev.next = None
            del current

    def length(self):
        """
        Returns the length of the linked list.

        Returns:
            int: The length of the linked list.

        Example:
        >>> my_list = LinkedList()
        >>> my_list.insertAtEnd(1)
        >>> my_list.insertAtEnd(2)
        >>> my_list.insertAtEnd(3)
        >>> my_list.length()
        3
        """
        ct = 0
        current = self.head
        while current:
            ct += 1
            current = current.next
        return ct