class Deque:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def insert_front(self,data):
        self.item.insert(0,data)

    def insert_rare(self,data):
        self.item.append(data)

    def delete_front(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            raise IndexError("list is empty")

    def delete_last(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("list is empty")

    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("list is empty")

    def get_rare(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("list is empty")

    def size(self):
        return len(self.item)


dq = Deque()
dq.insert_rare(1)
dq.insert_rare(2)
dq.insert_rare(3)
dq.insert_rare(4)
dq.insert_rare(5)
dq.insert_front(9)
dq.insert_front(8)
dq.insert_front(7)
dq.insert_front(6)
dq.delete_front()
dq.delete_last()
print(dq.get_front())
print(dq.get_rare())
print(dq.size())

