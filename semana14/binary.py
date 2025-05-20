class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left == None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right == None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def print_tree(self):
        self._print(self.root)

    def _print(self, node):
        if node != None:
            self._print(node.left)
            print(node.value)
            self._print(node.right)

bin_tree = BinaryTree()
bin_tree.insert(5)
bin_tree.insert(2)
bin_tree.insert(8)
bin_tree.insert(1)
bin_tree.insert(3)

bin_tree.print_tree()