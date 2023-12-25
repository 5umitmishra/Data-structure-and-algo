class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rare = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def insert_front(self,data):
        n = Node(None,data,self.front)
        if self.is_empty():
            self.rare = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count +=1

    def insert_rare(self,data):
        n = Node(data,self.rare)
        if self.is_empty():
            self.front = n
        else:
            self.rare.next = n
        self.rare = n
        self.item_count +=1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        if self.front == self.rare:
            self.front = None
            self.rare = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -=1

    def delete_rare(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        if self.front == self.rare:
            self.front = None
            self.rare = None
        else:
            self.rare = self.rare.prev
            self.rare.next = None
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        # else:
        return self.front.item

    def get_rare(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.rare.item

    def size(self):
        return self.item_count


dq = Deque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_front(30)
dq.insert_front(40)
print(dq.get_front(), dq.get_rare())
print(dq.item_count)
dq.delete_front()
dq.delete_rare()
print(dq.get_front())
print(dq.item_count)
print(dq.get_rare())


