class Node:
	def __init__(self) -> None:
		pass


class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        self.left = None
        self.right = None
    
    def get_node(self) -> any:
        return self.root
    
    def get_left(self) -> Node:
        return self.left
    
    def get_right(self) -> Node:
        return self.right
    
    def set_node(self, node):
        self.root = node

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

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

    # def balance(self, root):
    #     if root:
    #         return
    #     else:
    #         return 0

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

