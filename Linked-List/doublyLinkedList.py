from node import Node
    
class LinkedList(object):

    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        res = []
        while node:
            res.append(node.data)
            node = node.next
        if res:
            return " -> ".join(map(str, res))
        return "List is Empty!"

    def insertAtBegin(self, data):
        if self.head:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = Node(data)

    def insertAtIndex(self, data, index):
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
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)

    def updateNode(self, data, index):
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
        if self.head:
            current = self.head.next
            del self.head
            self.head = current
        else:
            print("List is Empty!")

    def removeNodeAtIndex(self, index):
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
        ct = 0
        current = self.head
        while current:
            ct += 1
            current = current.next
        return ct