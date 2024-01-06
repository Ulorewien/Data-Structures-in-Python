from linkedList import LinkedList
from circularLinkedList import CircularLinkedList
from doublyLinkedList import DoublyLinkedList

print("\nLINKED LIST : \n")

# Create a new linked list
ll = LinkedList()

# Insert elements at the beginning of the linked list
ll.insertAtBegin(1)
print("Insert 1 at start        :", ll)
ll.insertAtBegin(2)
print("Insert 2 at start        :", ll)
ll.insertAtBegin(3)
print("Insert 3 at start        :", ll)
ll.insertAtBegin(4)
print("Insert 4 at start        :", ll)
ll.insertAtBegin(5)
print("Insert 5 at start        :", ll)

# Insert an element at a specific index
ll.insertAtIndex(6, 3)
print("Insert 6 at 3rd index    :", ll)

# Insert an element at the end
ll.insertAtEnd(8)
print("Insert 8 at end          :", ll)

# Update an element at a specific index
ll.updateNode(100, 4)
print("Update 4th index to 100  :", ll)

# Remove the first node
ll.removeFirstNode()
print("Remove 1st node          :", ll)

# Remove nodes at specific indices
ll.removeFirstNode()
print("Remove 1st node          :", ll)
ll.removeFirstNode()
print("Remove 1st node          :", ll)
ll.removeNodeAtIndex(3)
print("Remove node at 3rd index :", ll)
ll.removeNodeAtIndex(0)
print("Remove node at 0th index :", ll)
ll.removeNodeAtIndex(2)
print("Remove node at 2nd index :", ll)

# Remove the last node
ll.removeLastNode()
print("Remove last node         :", ll)

# Remove the last node again
ll.removeLastNode()
print("Remove last node         :", ll)
print("\n")

print("\nCIRCULAR LINKED LIST : \n")

# Create a new circular linked list
cll = CircularLinkedList()

# Insert elements at the beginning of the circular linked list
cll.insertAtBegin(1)
print("Insert 1 at start        :", cll)
cll.insertAtBegin(2)
print("Insert 2 at start        :", cll)
cll.insertAtBegin(3)
print("Insert 3 at start        :", cll)
cll.insertAtBegin(4)
print("Insert 4 at start        :", cll)
cll.insertAtBegin(5)
print("Insert 5 at start        :", cll)

# Insert an element at a specific index
cll.insertAtIndex(6, 3)
print("Insert 6 at 3rd index    :", cll)

# Insert an element at the end
cll.insertAtEnd(8)
print("Insert 8 at end          :", cll)

# Update an element at a specific index
cll.updateNode(100, 4)
print("Update 4th index to 100  :", cll)

# Remove the first node
cll.removeFirstNode()
print("Remove 1st node          :", cll)

# Remove nodes at specific indices
cll.removeFirstNode()
print("Remove 1st node          :", cll)
cll.removeFirstNode()
print("Remove 1st node          :", cll)
cll.removeNodeAtIndex(3)
print("Remove node at 3rd index :", cll)
cll.removeNodeAtIndex(0)
print("Remove node at 0th index :", cll)
cll.removeNodeAtIndex(2)
print("Remove node at 2nd index :", cll)

# Remove the last node
cll.removeLastNode()
print("Remove last node         :", cll)

# Remove the last node again
cll.removeLastNode()
print("Remove last node         :", cll)
print("\n")

print("\nDOUBLY LINKED LIST : \n")

# Create a new doubly linked list
dll = DoublyLinkedList()

# Insert elements at the beginning of the doubly linked list
dll.insertAtBegin(1)
print("Insert 1 at start        :", dll)
dll.insertAtBegin(2)
print("Insert 2 at start        :", dll)
dll.insertAtBegin(3)
print("Insert 3 at start        :", dll)
dll.insertAtBegin(4)
print("Insert 4 at start        :", dll)
dll.insertAtBegin(5)
print("Insert 5 at start        :", dll)

# Insert an element at a specific index
dll.insertAtIndex(6, 3)
print("Insert 6 at 3rd index    :", dll)

# Insert an element at the end
dll.insertAtEnd(8)
print("Insert 8 at end          :", dll)

# Update an element at a specific index
dll.updateNode(100, 4)
print("Update 4th index to 100  :", dll)

# Print the doubly linked list in reverse order
print("Reverse List             :", dll.printReverse())

# Remove the first node
dll.removeFirstNode()
print("Remove 1st node          :", dll)

# Remove nodes at specific indices
dll.removeFirstNode()
print("Remove 1st node          :", dll)
dll.removeFirstNode()
print("Remove 1st node          :", dll)
dll.removeNodeAtIndex(3)
print("Remove node at 3rd index :", dll)
dll.removeNodeAtIndex(0)
print("Remove node at 0th index :", dll)
dll.removeNodeAtIndex(2)
print("Remove node at 2nd index :", dll)

# Remove the last node
dll.removeLastNode()
print("Remove last node         :", dll)

# Remove the last node again
dll.removeLastNode()
print("Remove last node         :", dll)
print("\n")
