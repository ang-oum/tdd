class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack items:", self.items)


# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
popped_item = stack.pop()
print("Popped item:", popped_item)
popped_item = stack.pop()
print("Popped item:", popped_item)
stack.display()