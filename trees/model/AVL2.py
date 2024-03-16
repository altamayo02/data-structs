class AVLNode:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        '''
        Retrieves the height of a tree, whether instanced or not.\n
        This is proven useful to check for heights of possibly null children.
        '''
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        # Rotation left
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        # Update heights of involved nodes
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def rotate_right(self, node):
        # Rotate right
        new_root = node.right 
        node.right = new_root.left
        new_root.left = node

        # Update heights of involved nodes
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def _add(self, root, value):
        if not root:
            # return AVL(value)
            return AVLNode(value)
        if value < root.value:
            root.left = self._add(root.left, value)
        else:
            root.right = self._add(root.right, value)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.balance(root)

        if balance > 1:
            if value < root.left.value:
                return self.rotate_left(root)
            else:
                root.left = self.rotate_right(root.left)
                return self.rotate_left(root)
        if balance < -1:
            if value > root.right.value:
                return self.rotate_right(root)
            else:
                root.right = self.rotate_left(root.right)
                return self.rotate_right(root)
        return root

    def add(self, value):
        '''
        Wrapper for the `_add` function.
        '''
        self.root = self._add(self.root, value)
    
    def _pre_order(self, root):
        if root is not None:
            print(root.value)
            self._pre_order(root.left)
            self._pre_order(root.right)

    def traverse(self, algo = "preorder"):
        if algo == "preorder":
            self._pre_order(self.root)

# Ejemplo de uso
arbol = AVL() 
arbol.add(10)
arbol.add(20)
arbol.add(5)
arbol.add(15)
arbol.add(18)
arbol.add(25)
arbol.traverse()