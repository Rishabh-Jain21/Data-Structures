class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def insertAtHead(self, value):
        if self.head == None:
            self.head = Node(value)
            self.count += 1
            return
        else:
            t = Node(value)
            t.right = self.head
            self.head = t
            self.count += 1

    def insertAtTail(self, value):
        if self.head == None:
            self.head = Node(value)
            self.count += 1
            return
        else:
            pointer = self.head
            while(pointer.right != None):
                pointer = pointer.right
            pointer.right = Node(value)
            self.count += 1

    def removeElement(self, value):
        previous = None
        current = self.head
        while(current != None):
            if(current.value == value):
                if previous != None:
                    previous.right = current.right
                else:
                    self.head = current.right
                self.count -= 1
                return True
            else:
                previous = current
                current = current.right
        return False

    def view(self):
        pointer = self.head
        while(pointer != None):
            print(pointer.value)
            pointer = pointer.right


li = LinkedList()
li.insertAtTail(55)
li.insertAtHead(4)
li.insertAtHead(5)
li.insertAtHead(6)
li.view()
li.insertAtHead(7)
li.insertAtTail(8)
li.insertAtHead(44)
print('-----')
li.view()
print(li.count)
li.removeElement(55)
li.insertAtHead(46)
print("-----")
li.view()
li.removeElement(8)
print()
li.view()
