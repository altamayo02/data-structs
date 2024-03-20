class BST:
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
                    root.set_left(BST(node))
            else:
                if root.get_right():
                    self.add(root.get_right(), node)
                else:
                    root.set_right(BST(node))

            return root
        return None

    # def in_order(self):
    #     return self._recursive_in_order(self.node)

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

    def min(self, root):
        if root:
            if not root.get_left():
                return root.get_node()
            return self.min(root.get_left())
        return None

    def max(self, root):
        if root:
            if not root.get_right():
                return root.get_node()
            return self.max(root.get_right())
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

    def balance(self, root):
        if root:
            return 
        else:
            return 0

    def levels(self, root):
        queue = [root]
        while queue:
            first = queue.pop(0)
            print(first.get_node())
            if first.get_left():
                queue.append(first.get_left())
            if first.get_right():
                queue.append(first.get_left())

    def branch(self, root):
        # This is private!!! Encapsulation!!!
        # Cierra el goteo (?)
        def visit_branch(root, branch, branches):
            if not root:
                return
            branch.append(root.get_node())
            if not root.get_left() and not root.get_right():
                branches.append(branch.copy())
            else:
                visit_branch(root.get_left(), branch, branches)
                visit_branch(root.get_right(), branch, branches)
            branch.pop()
        return visit_branch(root, [], [])

    # Habitual - Por la derecha
    def remove_node(self, root, node):
        if root:
            if node < root.get_node():
                root.set_left(self.remove_node(root.get_left(), node))
            elif node > root.get_node():
                root.set_right(self.remove_node(root.get_right(), node))
            else:
                if not root.get_left():
                    return root.get_right()
                elif not root.get_left():
                    return root.get_right()
                else:
                    root.set_node(self.min(root.get_right()))
                    root.set_right(self.remove_node(root.get_right(), root.get_node()))
        else:
            return None

