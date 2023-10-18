class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack."

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty stack."

# Example usage
stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Stack size:", stack.size())
print("Top element:", stack.peek())
popped_item = stack.pop()
print("\nPopped item:", popped_item)
print("\nStack size:", stack.size())
print("Top element:", stack.peek())

#----------------------------------------
stack1 = Stack()
print("\nStack size:", stack1.size())
popped_item = stack1.pop()
print("\nPopped item:", popped_item)