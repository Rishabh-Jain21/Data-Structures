class Minheaps:
    def __init__(self, items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatup(len(self.heap)-1)

    def push(self, data):
        self.heap.append(data)
        self.__floatup(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if(len(self.heap) > 2):
            self.__swap(1, len(self.heap)-1)
            min = self.heap.pop()
            self.__bubbledown(1)
        elif(len(self.heap) == 2):
            min = self.heap.pop()
        else:
            min = False
        return min

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatup(self, index):
        parent = index//2
        if index < 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__floatup(parent)

    def __str__(self):
        return str(self.heap)

    def __bubbledown(self, index):
        left = 2*index
        right = 2*index+1
        small = index
        if(len(self.heap) > left and self.heap[small] > self.heap[left]):
            small = left
        if len(self.heap) > right and self.heap[small] > self.heap[right]:
            small = right
        if small != index:
            self.__swap(index, small)
            self.__bubbledown(small)


m = Minheaps([97, 15, 26, 47, 12, 65, 47])
m.push(2)
print(m.pop())
print(m.push(1))
print(m)
