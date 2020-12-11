class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)


def maxDepth(node):
    if node is None:
        return 0
    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1


r = Node(1)
insert(r, Node(2))
insert(r, Node(3))
insert(r, Node(4))
insert(r, Node(5))
'''insert(r, Node(60))
insert(r, Node(80))


inorder(r)
print('---')
preorder(r)
print('---')
postorder(r)'''

print(maxDepth(r))
