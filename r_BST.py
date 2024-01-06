class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class R_BST:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)

        return self.__r_insert(self.root, value)

    def __r_contains(self, node, value):
        if node.value is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self.__r_contains(node.left, value)
        if value > node.value:
            return self.__r_contains(node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_inorder_traversal(self, current_node):
        if current_node:
            self.__r_inorder_traversal(current_node.left)
            print(current_node.value, end=" ")
            self.__r_inorder_traversal(current_node.right)

    def r_inorder_traversal(self):
        return self.__r_inorder_traversal(self.root)

    def get_mini(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def __r_delete_node(self, current_node, value):
        if current_node is None:
            return False
        if value < current_node.value:
            current_node.left = self.__r_delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete_node(current_node.right, value)
        else:
            if current_node.right is None and current_node.left is None:
                return None
            elif current_node.right is None:
                current_node = current_node.left
            elif current_node.left is None:
                current_node = current_node.right
            else:
                min_subtree = self.get_mini(current_node.right)
                current_node.value = min_subtree
                current_node.right = self.__r_delete_node(current_node.right, min_subtree)
        return current_node

    def r_delete(self, value):
        return self.__r_delete_node(self.root, value)


my_r_bst = R_BST()
my_r_bst.r_insert(40)
my_r_bst.r_insert(70)
my_r_bst.r_insert(10)
my_r_bst.r_insert(20)
my_r_bst.r_insert(15)
my_r_bst.r_insert(30)
my_r_bst.r_insert(5)

my_r_bst.r_delete(10)
print(my_r_bst.root.value)

my_r_bst.r_inorder_traversal()
