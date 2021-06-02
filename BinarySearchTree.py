from Node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        n = self.root
        while n is not None:
            if value > n.value:
                if n.right is None:
                    n.right = new_node
                    return
                n = n.right
            if value < n.value:
                if n.left is None:
                    n.left = new_node
                    return
                n = n.left

    def lookup(self, value):
        if value is None:
            return
        n = self.root
        while n is not None:
            if value > n.value:
                n = n.right
            if value < n.value:
                n = n.left
            if value == n.value:
                return n
        return None

    def remove(self, value):
        if self.root is None:
            return False
        current = self.root
        parent = None
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                # We have a match here

                # Option 1 No right child
                if current.right is None:
                    if parent is None:
                        self.root = current.left  # if user wants to delete root
                    else:
                        # if parent > current value, make current left child a child of parent
                        if parent.value > current.value:
                            parent.right = current.left
                        # if parent < current value, make left child a right child of parent
                        if parent.value < current.value:
                            parent.left = current.left
                # Option 2: Right child which doesnt have a left child
                elif current.right.left is None:
                    current.right.left = current.left
                    if parent is None:
                        self.root = current.right
                    else:
                        # if parent > current, make right child of the left the parent
                        if parent > current:
                            parent.left = current.right
                        # if parent < current, make right child a right child of the parent
                        elif parent < current:
                            parent.right = current.right
                # Option 3: Right child that has a left child
                else:
                    # Find the Right child's left most child
                    left_most = current.right.left
                    left_most_parent = current.right
                    while left_most.left is not None:
                        left_most_parent = left_most
                        left_most_child = left_most_child.left

                    # Parent's left subtree is now leftmost's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current.left
                    left_most.right = current.right

                    if parent is None:
                        self.root = left_most
                    else:
                        if current.value < parent.value:
                            parent.left = left_most
                        elif current.value > parent.value:
                            parent.right = left_most
                return True

    def traverse(self, node):
        tree = node
        tree.left = None if node.left is None else self.traverse(node.left)
        tree.right = None if node.right is None else self.traverse(node.right)
        return tree
