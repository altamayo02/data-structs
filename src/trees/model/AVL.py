class AVL:
    def __init__(self, node = None):
        self.node = node
        self.left = None
        self.right = None
        self.height = 0

    def get_height(self, root):
        '''
        Retrieves the height of a tree, whether instanced or not.\n
        This is proven useful to check for heights of possibly null children.
        '''
        if not root:
            return 0
        return root.height

    def balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_left(self, root):
        # Rotation left
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        # Update heights of involved nodes
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def rotate_right(self, root):
        # Rotation right
        new_root = root.right 
        root.right = new_root.left
        new_root.left = root

        # Update heights of involved nodes
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1
        return new_root

    def _add(self, root, node):
        if not root.node:
            return AVL(node)
        
        if node < root.node:
            root.left = self._add(root.left, node)
        else:
            root.right = self._add(root.right, node)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.balance(root)

        if balance > 1:
            if node < root.left.node:
                return self.rotate_left(root)
            else:
                root.left = self.rotate_right(root.left)
                return self.rotate_left(root)
        if balance < -1:
            if node > root.right.node:
                return self.rotate_right(root)
            else:
                root.right = self.rotate_left(root.right)
                return self.rotate_right(root)
        return root

    def add(self, node):
        '''
        Wrapper for the `_add` function.
        '''
        # FIXME
        self = self._add(self, node)
    
    def _pre_order(self, root):
        if root is not None:
            print(root.node)
            self._pre_order(root.left)
            self._pre_order(root.right)

    def traverse(self, algo = "preorder"):
        if algo == "preorder":
            self._pre_order(self)

# Ejemplo de uso
arbol = AVL()
arbol.add(10)
arbol.add(20)
arbol.add(5)
arbol.add(15)
arbol.add(18)
arbol.add(25)
arbol.traverse()