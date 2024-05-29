class Node:
    def __init__(self, key, color="red"):
        self.key = key
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = "black"
        self.root = self.TNULL

    def insert(self, key):
        node = Node(key)
        node.left = self.TNULL
        node.right = self.TNULL

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = "red"
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def in_order_traversal(self, node):
        if node != self.TNULL:
            self.in_order_traversal(node.left)
            print(f"{node.key} ({'R' if node.color == 'red' else 'B'})", end=" ")
            self.in_order_traversal(node.right)

    def print_tree(self):
        self.in_order_traversal(self.root)
        print()

# Testing the Red-Black Tree Implementation
def test_red_black_tree():
    rbt = RedBlackTree()
    
    # Insert some keys
    keys = [20, 15, 25, 10, 5, 1, 30, 35, 25, 40]
    for key in keys:
        rbt.insert(key)
        print(f"Inserted {key}:")
        rbt.print_tree()

test_red_black_tree()
