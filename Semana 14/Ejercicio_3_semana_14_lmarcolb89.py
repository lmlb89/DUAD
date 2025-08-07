# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#    1. Debe incluir un método para hacer `print` de toda la estructura.
#    2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTreeNode(value)
        else:
            new_node = BinaryTreeNode(value)
            new_node.left = self.left
            self.left = new_node
    
    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTreeNode(value)
        else:
            new_node = BinaryTreeNode(value)
            new_node.right = self.right
            self.right = new_node
    
    def print_tree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.value))
        if self.left is not None:
            self.left.print_tree(level + 1, "L--- ")
        if self.right is not None:
            self.right.print_tree(level + 1, "R--- ")

class BinaryTree:
    def __init__(self, root_value):
        self.root = BinaryTreeNode(root_value)
    
    def print_tree(self):
        if self.root is not None:
            self.root.print_tree()
        else:
            print("Tree is empty")


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.insert_left(2)
    tree.root.insert_right(3)
    tree.root.left.insert_left(4)
    tree.root.left.insert_right(5)
    tree.root.right.insert_left(6)
    tree.root.right.insert_right(7)
    
    tree.print_tree()
