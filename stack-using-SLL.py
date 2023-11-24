# Here we implement stack by using singly linked list

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None

    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1
        return data

    def pop(self):
        if self.start == None:
            raise IndexError("stack is empty")
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self.start.item

    def size(self):
        return self.item_count


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.pop())

