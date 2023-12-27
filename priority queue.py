class Priority:
    def __init__(self):
        self.item = []

    def push(self,data,priority):
        index = 0
        while index < len(self.item) and self.item[index][1] <= priority:
            index += 1
        self.item.insert(index,(data, priority))

    def is_empty(self):
        return len(self.item) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("data is empty")
        else:
            return self.item.pop(0)[0]

    def size(self):
        return len(self.item)

p = Priority()
p.push("sumit",1)
p.push("ganesh",3)
p.push("ayush",2)
p.push("nikki",2)
p.push("shruti",2)
# print(p.item)
# print(p.size())
while not p.is_empty():
    print(p.pop())

# print(p)



