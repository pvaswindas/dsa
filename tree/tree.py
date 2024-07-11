class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add_value(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.initialize(data, self.root)

    def visit(self, node):
        print(node.data)

    def initialize(self, data, root):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self.initialize(data, root.left)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self.initialize(data, root.right)

    def preorder(self, root):
        if root is None:
            return
        self.visit(root)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.visit(root)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.visit(root)

    def find_min(self, root):
        node = root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    def scnd_min(self, root):
        node = root
        if node is None:
            return None
        if node.left is None:
            return node.data
        scnd_small = None
        small = node.data
        while node:
            scnd_small = small
            small = node.data
            node = node.left
        return scnd_small

    def find_max(self):
        node = self.root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node

    def scnd_max(self):
        node = self.root
        if node is None:
            return None
        if node.right is None:
            return node.left.data
        scnd_lrg = None
        lrg = node.data
        while node:
            scnd_lrg = lrg
            lrg = node.data
            node = node.right
        return scnd_lrg

    def deletenode(self, root, val):
        if root is None:
            return root
        if val < root.data:
            root.left = self.deletenode(root.left, val)
        elif val > root.data:
            root.right = self.deletenode(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_val = self.find_min(root.right)
            root.data = min_val.data
            root.right = self.deletenode(root.right, min_val.data)
        return root

    def find_closest_value(self, target):
        return self._find_closest_value(self.root, target, float('inf'))

    def _find_closest_value(self, root, target, closest):
        if root is None:
            return closest
        if abs(target - closest) > abs(target - root.data):
            closest = root.data
        if target < root.data:
            return self._find_closest_value(root.left, target, closest)
        elif target > root.data:
            return self._find_closest_value(root.right, target, closest)
        else:
            return closest


tree = Tree()
tree.add_value(5)
tree.add_value(10)
tree.add_value(6)
tree.add_value(88)
tree.add_value(2000)
tree.add_value(4)
tree.add_value(1)
tree.add_value(2)
tree.add_value(8)
tree.add_value(9)
tree.add_value(500)
tree.add_value(3)
tree.inorder(tree.root)
tree.deletenode(tree.root, 88)
print()
tree.inorder(tree.root)
print()
print(tree.find_closest_value(7))
