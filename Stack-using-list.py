class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("stack is empty")

    def size(self):
        return len(self.item)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element is", stack.peek())
print("removed element is", stack.pop())
print("Top element is", stack.peek())
print()