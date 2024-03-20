import AVL

class AVL:
	def __init__(self, node: int = None):
		self.node = node
		self.left = None
		self.right = None
		self.height = 1
	
	def get_node(self) -> int:
		return self.node
	
	def set_node(self, node):
		self.node = node

	def get_left(self) -> AVL:
		return self.left
	
	def set_left(self, left):
		self.left = left

	def get_right(self) -> AVL:
		return self.right
	
	def set_right(self, right):
		self.right = right

	def get_height(self) -> int:
		return self.height
	
	def set_height(self, height):
		self.height = height



	def balance(self, root: AVL):
		if not root:
			return 0
		return root.get_left() - root.get_right()

	def rotate_left(self, root: AVL):
		# Rotation left
		new_root = root.get_left()
		root.set_left(new_root.get_right())
		new_root.set_right(root)

		# Update heights of involved nodes
		root.set_height(max(AVL(root.get_left()), AVL(root.get_right())) + 1)
		new_root.set_height(max(AVL(new_root.get_left()), AVL(new_root.get_right())) + 1)
		return new_root

	def rotate_right(self, root: AVL):
		# Rotate right
		new_root = root.get_right() 
		root.set_right(new_root.get_left())
		new_root.set_left(root)

		# Update heights of involved nodes
		root.set_height(max(AVL(root.get_left()), AVL(root.get_right())) + 1)
		new_root.set_height(max(new_root.get_left(), new_root.get_right()) + 1)
		return new_root

	def _add(self, root: AVL, node: int):
		if not root:
			return AVL(node)
		print(root)
		if node < root.get_node():
			root.set_left(self._add(root.get_left(), node))
		else:
			root.set_right(self._add(root.get_right(), node))

		root.set_height(max((root.get_left()), (root.get_right())) + 1)
		balance = self.balance(root)

		if balance > 1:
			if node < root.get_left().get_node():
				return self.rotate_left(root)
			else:
				root.set_left(self.rotate_right(root.get_left()))
				return self.rotate_left(root)
		if balance < -1:
			if node > root.get_right().get_node():
				return self.rotate_right(root)
			else:
				root.set_right(self.rotate_left(root.get_right()))
				return self.rotate_right(root)
		return root

	def add(self, node: int):
		self.set_node(self._add(self.get_node(), node))
	
	def _pre_order(self, root: AVL):
		if root is not None:
			print(root.get_node())
			self._pre_order(root.get_left())
			self._pre_order(root.get_right())

	def traverse(self, algo: str = "preorder"):
		if algo == "preorder":
			self._pre_order(self.get_node())



	def __gt__(self, other: AVL):
		return (self.get_height() or 0) > (other.get_height() or 0)

	def __gt__(self, number: int):
		return (self.get_height() or 0) > (number or 0)

	def __lt__(self, other: AVL):
		return (self.get_height() or 0) < (other.get_height() or 0)

	def __lt__(self, number: int):
		return (self.get_height() or 0) < (number or 0)
	
	'''
	Used in max(a: AVL, b: AVL)
	'''
	def __add__(self, other: AVL):
		return (self.get_height() or 0) + (other.get_height() or 0)

	def __add__(self, number: int):
		return (self.get_height() or 0) + (number or 0)
	
	def __sub__(self, other: AVL):
		return (self.get_height() or 0) - (other.get_height() or 0)

	def __sub__(self, number: int):
		return (self.get_height() or 0) - (number or 0)
	
	def __rsub__(self, other: AVL):
		return (self.get_height() or 0) - (other.get_height() or 0)

	def __rsub__(self, number: int):
		return (number or 0) - (self.get_height() or 0)

# Ejemplo de uso
avl = AVL()
avl.add(10)
avl.add(20)
avl.add(5)
avl.add(15)
avl.add(18)
avl.add(25)
avl.traverse()