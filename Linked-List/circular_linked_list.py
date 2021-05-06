class Node(object):
    def __init__(self, key, next):
        self.key = key
        self.next = next


class Linked_List():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, key):
        new_node = Node(key, None)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            self.size += 1
            return
        p = self.head
        new_node.next = self.head
        while p.next != self.head:
            p = p.next
        p.next = new_node
        self.size += 1
        self.head = new_node
        return

    def display(self):
        if not self.size:
            print("Empty List")
            return
        p = self.head
        while p.next != self.head:
            print(p.key, end="-->")
            p = p.next
        print(p.key)
        return

    def insert_at_tail(self, key):
        new_node = Node(key, None)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            self.size += 1
            return
        p = self.head
        new_node.next = self.head
        while p.next != self.head:
            p = p.next
        p.next = new_node
        self.size += 1
        return

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
            print("Empty List")
            return

        p = self.head
        while p.next != self.head:
            p = p.next
        p.next = self.head.next
        self.head = p.next
        self.size -= 1

    def delete_at_tail(self):
        if not self.head:
            print("Empty List")
            return
        p = self.head
        i = 1
        while i < (self.size-1):
            print("Key is", p.key)
            p = p.next
            i = i+1
        p.next = self.head
        self.size -= 1

    def search(self, key):
        if not self.head:
            print("List is empyty")
            return
        p = self.head
        while p.next != self.head:
            if p.key == key:
                return("Key Found")
            p = p.next
        if p.key == key:
            return("Key Found")
        return "Key Not Found"

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


l = Linked_List()
l.insert_at_head(4)
l.insert_at_head(3)

l.display()
l.delete_any_position(1)
l.display()
