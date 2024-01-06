class Queue(object):
    """
    A simple implementation of a queue data structure.

    Attributes:
        queue (list): A list to store elements in the queue.

    Methods:
        __init__(): Initializes an empty queue.
        __repr__(): Returns a string representation of the elements in the queue.
        enqueue(val): Adds the specified value to the end of the queue.
        dequeue(): Removes and returns the element from the front of the queue.
        isEmpty(): Checks if the queue is empty.
    """

    def __init__(self):
        """
        Initializes an empty queue.

        Example:
        >>> my_queue = Queue()
        """
        self.queue = []

    def __repr__(self):
        """
        Returns a string representation of the elements in the queue.

        Returns:
            str: A space-separated string representation of the elements in the queue.

        Example:
        >>> my_queue = Queue()
        >>> my_queue.enqueue(1)
        >>> my_queue.enqueue(2)
        >>> my_queue.enqueue(3)
        >>> print(repr(my_queue))
        '1 2 3'
        """
        return " ".join(map(str, self.queue))

    def enqueue(self, val):
        """
        Adds the specified value to the end of the queue.

        Args:
            val: The value to be added to the queue.

        Example:
        >>> my_queue = Queue()
        >>> my_queue.enqueue(42)
        """
        self.queue.append(val)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
            The element removed from the front of the queue.

        Raises:
            Exception: If the queue is empty.

        Example:
        >>> my_queue = Queue()
        >>> my_queue.enqueue(1)
        >>> my_queue.enqueue(2)
        >>> dequeued_element = my_queue.dequeue()
        """
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def isEmpty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.

        Example:
        >>> my_queue = Queue()
        >>> is_empty = my_queue.isEmpty()
        """
        if self.queue:
            return False
        return True