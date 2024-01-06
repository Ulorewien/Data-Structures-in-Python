from queue import Queue

# Create a new Queue instance
q = Queue()

# Add 1 to the queue and print the result (None)
print("Add 1   : ", q.enqueue(1))

# Add 2 to the queue and print the result (None)
print("Add 2   : ", q.enqueue(2))

# Add 5 to the queue and print the result (None)
print("Add 5   : ", q.enqueue(5))

# Add 7 to the queue and print the result (None)
print("Add 7   : ", q.enqueue(7))

# Print the contents of the queue
print("Queue   : ", q)

# Remove and print the element from the front of the queue (1)
print("Dequeue : ", q.dequeue())

# Check if the queue is empty and print the result (False)
print("Empty   : ", q.isEmpty())

# Remove and print the element from the front of the queue (2)
print("Dequeue : ", q.dequeue())

# Remove and print the element from the front of the queue (5)
print("Dequeue : ", q.dequeue())

# Remove and print the element from the front of the queue (7)
print("Dequeue : ", q.dequeue())

# Check if the queue is empty and print the result (True)
print("Empty   : ", q.isEmpty())

# Try to remove an element from an empty queue, raising an exception
# (uncommenting the line below will result in an Exception)
# print("Dequeue : ", q.dequeue())
