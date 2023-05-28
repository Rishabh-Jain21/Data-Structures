# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to print the root-to-leaf path with a given sum in a binary tree
def printPath(root, sum):

    # base case
    if sum == 0:
        return True

    # base case
    if root is None:
        return False

    # recur for the left and right subtree with reduced sum
    left = printPath(root.left, sum - root.data)
    right = printPath(root.right, sum - root.data)

    # print the current node if it lies on a path with a given sum
    if left or right:
        print(root.data, end=' ')

    return left or right


# Function to calculate the maximum root-to-leaf sum in a binary tree
def getRootToLeafSum(root, s, lst):

    # base case: tree is empty
    if root is None:
        return [s, lst[:]]

    # calculate the maximum node-to-leaf sum for the left child
    k = lst[:]
    k.append(root.data)
    su = s+root.data
    left = getRootToLeafSum(root.left, su, k)

    # calculate the maximum node-to-leaf sum for the right child
    right = getRootToLeafSum(root.right, su, k)

    # consider the maximum sum child
    if left[0] > right[0]:
        return left
    return right


# Function to print maximum sum root-to-leaf path in a given binary tree
def findMaxSumPath(root):

    sum = getRootToLeafSum(root, 0, [])

    print("The maximum sum is", sum)
    # print("The maximum sum path is ", end='')

    # printPath(root, sum)


if __name__ == '__main__':

    root = None
    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        8   4   5   6
           /   / \   \
         10   7   9   5
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(8)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(10)
    root.right.left.left = Node(7)
    root.right.left.right = Node(9)
    root.right.right.right = Node(5)

    findMaxSumPath(root)
