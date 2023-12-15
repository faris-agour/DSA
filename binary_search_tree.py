class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if node.value == temp.value:
                return False

            if node.value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left

            if node.value > temp.value:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right

    def contain(self, item):
        temp = self.root
        while temp:
            if self.root is None:
                return False

            if item == temp.value:
                return True

            if item < temp.value:
                temp = temp.left

            if item > temp.value:
                temp = temp.right
        return False

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)

            print(root.value, end=' ')

            self.inorder_traversal(root.right)


bst = BST()
bst.insert(2)
bst.insert(3)
bst.insert(22)
bst.insert(1)
bst.insert(11)
bst.insert(134)

print(bst.contain(1))
bst.inorder_traversal(bst.root)
