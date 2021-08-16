class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items


def balancing(arr):

    if len(arr)%2 != 0:
        return False
    
    opening = set('([{')
    matches = set([("(",")"), ("[","]"), ("{","}")])

    s = Stack()
    
    for i in arr:
        
        if i in opening:
            s.push(i)
        else:
            if s.size() == 0:
                return False
            
            last_open = s.pop()

            if (last_open, i) not in matches:
                return False
            
    return s.size() == 0


print(balancing("({[}])"))
