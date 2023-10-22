""" singly linked list """
class Node:
    def __init__(self,item = None, next = None):
        self.item = item
        self.next = next
class SLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_in_start(self, data):
        n = Node(data,self.start)
        self.start = n

    def insert_in_last(self,data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp,data):
        n = Node(data, temp.next)
        temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_frisr(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    # here we make our code iterable
    def __iter__(self):
        return SLLIterator(self.start)
class SLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# driver code
my_list = SLL()
my_list.insert_in_start(20)
my_list.insert_in_start(10)
my_list.insert_in_last(30)
my_list.insert_in_last(31)

my_list.insert_after(my_list.search(20), 25)
my_list.print_list()
print()
my_list.delete_item(31)
for x in my_list:
    print(x, end=' ')
