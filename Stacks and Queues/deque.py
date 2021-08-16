class Deque(object):
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        return self.items.append(item)
    
    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items

d = Deque()

print(d.isEmpty())

d.addFront(5)
d.addFront(7)
d.addFront(4)
d.addRear(9)

print(d.show())

d.removeFront()
d.removeRear()

print(d.show())

print(d.size())