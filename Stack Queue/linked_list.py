class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
print(a.value)
print(a.nextnode.value)
print(a.nextnode.nextnode.value)
#print(a.nextnode.nextnode.nextnode.value)
