class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinaryTrees():
    def __init__(self):
        self.root = None

    def iterative_insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            t = self.root
            while t:
                if key == t.key:
                    return False
                elif key > t.key:
                    if not t.right:
                        t.right = Node(key)
                    else:
                        t = t.right
                elif key < t.key:
                    if not t.left:
                        t.left = Node(key)
                    else:
                        t = t.left

    def recursive_insert(self, troot, key):
        if troot:
            if troot.key == key:
                return False
            elif troot.key > key:
                if not troot.left:
                    troot.left = Node(key)
                else:
                    self.recursive_insert(troot.left, key)
            elif troot.key < key:
                if not troot.right:
                    troot.right = Node(key)
                else:
                    self.recursive_insert(troot.right, key)
        else:
            self.root = Node(key)

    def count(self, troot):
        if troot:
            x = self.count(troot.left)
            y = self.count(troot.right)
            return x+y+1
        return 0

    def height(self, troot):
        if troot:
            x = self.height(troot.left)
            y = self.height(troot.right)
            print(x, y)
            return max(x, y)+1
        return 0

    def preorder(self, troot):
        if troot:
            print(troot.key)
            self.preorder(troot.left)
            self.preorder(troot.right)

    def inorder(self, troot):
        if troot:
            self.inorder(troot.left)
            print(troot.key)
            self.inorder(troot.right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.key)

    def level_order(self):
        queue = []
        t = self.root
        print(self.root.key)
        queue.append(t)
        while queue:
            element = queue.pop(0)
            if element.left:
                print(element.left.key)
                queue.append(element.left)
            if element.right:
                print(element.right.key)
                queue.append(element.right)

    def iterative_search(self, key):
        t = self.root
        while t:
            if t.key == key:
                return True
            elif t.key < key:
                t = t.right
            elif t.key > key:
                t = t.left
        return False

    def recursive_search(self, troot, key):
        if troot:
            if troot.key == key:
                print(troot.key)
                return True
            elif troot.key > key:
                return self.recursive_search(troot.left, key)
            elif troot.key < key:
                return self.recursive_search(troot.right, key)
        return False

    def delete(self, key):
        p = self.root
        while p and p.key != key:
            pp = p
            if p.key < key:
                p = p.right
            elif p.key > key:
                p = p.left
        if not p:
            return False

        if p.left and p.right:
            s = p.left
            ps = p
            while s.right:
                ps = s
                s = s.right

            p.element = s.element
            p = s
            pp = ps
        c = None
        if p.left:
            c = p.left
        else:
            c = p.right
        if p == self.root:
            self.root = None
        else:
            if p == pp.left:
                pp.left = c
            else:
                pp.right = c


b = BinaryTrees()
b.recursive_insert(b.root, 15)
b.iterative_insert(20)
b.iterative_insert(10)
b.recursive_insert(b.root, 30)
b.inorder(b.root)
print()
b.preorder(b.root)
print()
b.postorder(b.root)
print(b.height(b.root))
print(b.iterative_search(10))
print(b.iterative_search(8))
print(b.recursive_search(b.root, 30))
print(b.recursive_search(b.root, 50))
b.delete(20)
print()
(b.inorder(b.root))
print()
b.level_order()
print()
b1 = BinaryTrees()
for i in [20, 10, 30, 5, 11, 37, 6]:
    b1.iterative_insert(i)

b1.level_order()
