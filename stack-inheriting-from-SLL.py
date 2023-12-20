from assign3 import *

class stack:
    def __init__(self):
        self.mylist =SLL
        self.item_count =0

    def is_empty(self):
        return self.mylist.is_empty()

    def push(self,data):
        self.mylist.insert_in_start(data)
        self.item_count +=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_frisr()
            self.item_count -=1
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.mylist.item
        else:
            raise IndexError("stack is empty")

    def size(self):
        return self.item_count
