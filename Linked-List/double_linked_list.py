class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Linked_List():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_tail(self, key):
        new_node = Node(key)
        if not self.head:
            self.head = Node(key)
            self.size += 1
            return

        p = self.head
        while p.right:
            p = p.right
        p.right = new_node
        new_node.left = p
        self.size += 1

    def display(self):
        p = self.head
        if not p:
            print("Linked List is empty")
            return
        while p.right:
            print(p.key, end="-->")
            p = p.right
        print(p.key)

    def insert_at_head(self, key):
        new_node = Node(key)
        if not self.head:
            self.head = Node(key)
            self.size += 1
            return
        new_node = Node(key)
        p = self.head
        p.left = new_node
        new_node.right = self.head
        self.head = new_node
        self.size += 1

    def insert_at_any_postition(self, key, position):
        if position == 1:
            return self.insert_at_head(key)
        if position == self.size:
            return self.insert_at_tail(key)
        new_node = Node(key)
        p = self.head
        i = 1
        while i < (position-1):
            p = p.right
            i = i+1
        new_node.right = p.right
        p.right = new_node
        new_node.left = p
        self.size += 1

    def delete_at_head(self):
        if not self.head:
            print("Empty List")
            return
        self.head = self.head.right
        self.head.left = None
        self.size -= 1

    def delete_at_tail(self):
        if not self.head:
            print("Empty List")
            return
        p = self.head
        i = 1
        while i < (self.size-1):
            p = p.right
            i = i+1
        p.right = None
        self.size -= 1

    def delete_at_any_position(self, position):
        if not self.head:
            print("List is empty")
            return
        if position == 1:
            return self.delete_at_head()

        if position == self.size:
            return self.delete_at_tail()

        if not 1 <= position <= self.size:
            print("Position Invalid")
            return
        p = self.head
        i = 1
        while i < position-1:
            p = p.next
            i = i+1
        p.right = p.right.right
        (p.right).left = p
        self.size -= 1


l = Linked_List()
l.display()

l.insert_at_tail(1)
l.insert_at_tail(2)
l.display()
l.insert_at_head(3)
l.display()
l.insert_at_head(77)
l.display()
print(l.size)
l.insert_at_any_postition(9, 3)
l.display()
l.delete_at_head()
l.display()
l.insert_at_head(45)
l.display()
l.delete_at_tail()
l.display()
l.delete_at_any_position(2)
l.display()
