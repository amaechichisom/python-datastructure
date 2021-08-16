class Queue2Stacks(object):
    def __init__(self) -> None:
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def queue(self, element):

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop() 