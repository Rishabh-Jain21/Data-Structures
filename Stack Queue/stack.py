class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def peep(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


'''
s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
print(s.pop())
print(s.peep())
s.push(4)
print(s.pop())
'''
