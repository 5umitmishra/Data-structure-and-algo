class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def enqueue(self,data):
        self.item.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            raise IndexError("queue is empty")

    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("queue is empty")

    def size(self):
        return len(self.item)

my_queue = Queue()
my_queue.enqueue(50)
my_queue.enqueue(60)
my_queue.enqueue(70)
print(my_queue.size())
print(my_queue.item)
my_queue.dequeue()
print(my_queue.item)
print(my_queue.size())
print(my_queue.get_front())
print(my_queue.get_rear())