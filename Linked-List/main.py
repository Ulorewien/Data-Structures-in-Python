from linkedList import LinkedList
from circularLinkedList import CircularLinkedList

print("\nLINKED LIST : \n")

ll = LinkedList()
ll.insertAtBegin(1)
print("Insert 1 at start        :",ll)
ll.insertAtBegin(2)
print("Insert 2 at start        :",ll)
ll.insertAtBegin(3)
print("Insert 3 at start        :",ll)
ll.insertAtBegin(4)
print("Insert 4 at start        :",ll)
ll.insertAtBegin(5)
print("Insert 5 at start        :",ll)
ll.insertAtIndex(6,3)
print("Insert 6 at 3rd index    :",ll)
ll.insertAtIndex(7,6)
print("Insert 7 at 6th index    :",ll)
print("Length                   :",ll.length())
ll.insertAtEnd(8)
print("Insert 8 at end          :",ll)
ll.updateNode(100, 4)
print("Update 4th index to 100  :",ll)
ll.removeFirstNode()
print("Remove 1st node          :",ll)
ll.removeFirstNode()
print("Remove 1st node          :",ll)
ll.removeFirstNode()
print("Remove 1st node          :",ll)
ll.removeNodeAtIndex(3)
print("Remove node at 3rd index :",ll)
ll.removeNodeAtIndex(0)
print("Remove node at 0th index :",ll)
ll.removeNodeAtIndex(2)
print("Remove node at 2nd index :",ll)
ll.removeLastNode()
print("Remove last node         :",ll)
ll.removeLastNode()
print("Remove last node         :",ll)
print("\n")

print("\nCIRCULAR LINKED LIST : \n")

ll = CircularLinkedList()
ll.insertAtBegin(1)
print("Insert 1 at start        :",ll)
ll.insertAtBegin(2)
print("Insert 2 at start        :",ll)
ll.insertAtBegin(3)
print("Insert 3 at start        :",ll)
ll.insertAtBegin(4)
print("Insert 4 at start        :",ll)
ll.insertAtBegin(5)
print("Insert 5 at start        :",ll)
ll.insertAtIndex(6,3)
print("Insert 6 at 3rd index    :",ll)
ll.insertAtIndex(7,6)
print("Insert 7 at 6th index    :",ll)
print("Length                   :",ll.length())
ll.insertAtEnd(8)
print("Insert 8 at end          :",ll)
ll.updateNode(100, 4)
print("Update 4th index to 100  :",ll)
ll.removeFirstNode()
print("Remove 1st node          :",ll)
ll.removeFirstNode()
print("Remove 1st node          :",ll)
ll.removeFirstNode()
print("Remove 1st node          :",ll)
ll.removeNodeAtIndex(3)
print("Remove node at 3rd index :",ll)
ll.removeNodeAtIndex(0)
print("Remove node at 0th index :",ll)
ll.removeNodeAtIndex(2)
print("Remove node at 2nd index :",ll)
ll.removeLastNode()
print("Remove last node         :",ll)
ll.removeLastNode()
print("Remove last node         :",ll)
print("\n")