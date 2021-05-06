class MaxHeap():
    def __init__(self):
        self.items = [-1]

    def insert(self, key):
        self.items.append(key)
        index = len(self.items)-1
        while index > 1 and self.items[index//2] < key:
            self.items[index] = self.items[index//2]
            index = index//2
        self.items[index] = key

    def delete(self):
        self.items[1], self.items[len(
            self.items)-1] = self.items[len(self.items)-1], self.items[1]

        value = self.items.pop()
        i = 1
        j = i*2
        while j < len(self.items)-1:
            if self.items[j] < self.items[j+1]:
                j = j+1
            if self.items[i] < self.items[j]:
                self.items[i], self.items[j] = self.items[j], self.items[i]
                i = j
                j = j*2
            else:
                break
        return value

    def peek(self):
        if len(self.items) == 1:
            return False
        return self.items[1]

    def show(self):
        print(self.items)


a = MaxHeap()
print(a.peek())
a.insert(4)
a.show()
a.insert(5)
a.insert(6)
a.insert(8)
a.insert(1)
a.show()
a.insert(45)
a.show()
a.insert(36)
a.show()
a.insert(40)
a.show()
print(a.peek())
a.delete()
a.show()
