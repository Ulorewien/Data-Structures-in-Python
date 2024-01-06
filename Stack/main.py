from stack import Stack

# Create a new stack instance
s = Stack()

# Push 1 onto the stack and print the result (None)
print("Push 1      : ", s.push(1))

# Push 2 onto the stack and print the result (None)
print("Push 2      : ", s.push(2))

# Push 5 onto the stack and print the result (None)
print("Push 5      : ", s.push(5))

# Push 7 onto the stack and print the result (None)
print("Push 7      : ", s.push(7))

# Pop an element from the stack and print the result (7)
print("Pop         : ", s.pop())

# Get the element at the top of the stack and print the result (5)
print("Top         : ", s.top())

# Check if the stack is empty and print the result (False)
print("Is empty    : ", s.isEmpty())

# Get the size of the stack and print the result (2)
print("Size        : ", s.size())

# Pop an element from the stack and print the result (2)
print("Pop         : ", s.pop())

# Pop an element from the stack and print the result (1)
print("Pop         : ", s.pop())

# Pop an element from the stack and print the result (None) - stack is now empty
print("Pop         : ", s.pop())

# Check if the stack is empty and print the result (True)
print("Is empty    : ", s.isEmpty())

# Get the size of the stack and print the result (0)
print("Size        : ", s.size())

# Try to pop an element from an empty stack, raising an exception
# (uncommenting the line below will result in an Exception)
# print("Pop         : ", s.pop())

# Try to get the element at the top of an empty stack, raising an exception
# (uncommenting the line below will result in an Exception)
# print("Top         : ", s.top())