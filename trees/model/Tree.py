class Tree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None
    
    def get_node(self):
        return self.node
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_node(self, node):
        self.node = node

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right



    def add(self, root, node):
        if root:
            if node == root.node:
                return root

            if node < root.node:
                if root.get_left():
                    self.add(root.get_left(), node)
                else:
                    root.set_left(Tree(node))
            else:
                if root.get_right():
                    self.add(root.get_right(), node)
                else:
                    root.set_right(Tree(node))

            return root
        return None

    def in_order(self, root):
        if root:
            return (
                self.in_order(root.get_left()) +
                [root.get_node()] +
                self.in_order(root.get_right())
            )
        return []
        
    def pre_order(self, root):
        if root:
            return (
                [root.get_node()] +
                self.pre_order(root.get_left()) +
                self.pre_order(root.get_right())
            )
        return []

    def post_order(self, root):
        if root:
            return (
                self.post_order(root.get_left()) +
                self.post_order(root.get_right()) +
                [root.get_node()]
            )
        return []
        
    def height(self, root):
        if root:
            return max(
                self.height(root.get_left()) + 1,
                self.height(root.get_right()) + 1
            )
        return 0

    def weight(self, root):
        if root:
            return 1 + (
                self.weight(root.get_left()) +
                self.weight(root.get_right())
            )
        return 0

    def lessest(self, root):
        if root:
            if not root.get_left():
                return root.get_node()
            return self.lessest(root.get_left())
        return None

    def greatest(self, root):
        if root:
            if not root.get_right():
                return root.get_node()
            return self.greatest(root.get_right())
        return None

    def exists(self, root, node):
        if root:
            if node == root.get_node():
                return True
            
            if node < root.get_node():
                return self.exists(root.get_left(), node)
            else:
                return self.exists(root.get_right(), node)

        return False