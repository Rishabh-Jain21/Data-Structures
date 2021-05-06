class Node(object):
    def __init__(self, key, next):
        self.key = key
        self.next = next


class Linked_List():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, element):
        new_node = Node(element, None)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = new_node
        self.size += 1

    def display(self):
        p = self.head
        if not p:
            print("Linked List is empty")
            return
        while p.next:
            print(p.key, end="-->")
            p = p.next
        print(p.key)

    def insert_at_tail(self, element):
        new_node = Node(element, None)
        p = self.head
        if not p:
            self.head = new_node
            self.size = self.size+1
            return
        while p.next:
            p = p.next
        p.next = new_node
        self.size = self.size+1

    def insert_any_position(self, element, position):
        if position == 1:
            return self.insert_at_head(element)
        if position == self.size:
            return self.insert_at_tail(element)

        new_node = Node(element, None)
        p = self.head
        i = 1
        while i < position-1:
            p = p.next
            i = i+1
        new_node.next = p.next
        p.next = new_node
        self.size += 1

    def delete_at_head(self):
        if not self.head:
            print("List is empty")
            return
        p = self.head
        ele = p.key
        self.head = self.head.next
        self.size -= 1
        return ele

    def delete_at_tail(self):
        if not self.head:
            print("List is empty")
            return
        i = 1
        p = self.head
        print(self.size)
        while i < (self.size-1):
            p = p.next
            i = i+1
        ele = p.next.key
        p.next = None
        self.size -= 1
        return ele

    def delete_any_position(self, position):
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
        ele = p.next.key
        p.next = p.next.next
        self.size -= 1
        return ele

    def search(self, key):
        if not self.head:
            print("List is empyty")
            return
        p = self.head
        while p:
            if p.key == key:
                return("Key Found")
            p = p.next

        return "Key Not Found"


l = Linked_List()
l.display()
l.insert_at_tail(10)
l.display()
l.insert_at_head(4)
l.insert_at_head(7)
l.display()
l.insert_at_tail(8)
l.display()
l.insert_any_position(11, 2)
l.display()
print(l.delete_at_tail())
l.insert_at_tail(17)
l.display()
l.insert_at_tail(99)
l.display()
l.delete_any_position(2)
l.display()
l.delete_any_position(1)
l.display()
l.delete_any_position(4)
l.display()
l.insert_any_position(4, 2)
print(l.search(17))
l.delete_any_position(14)
