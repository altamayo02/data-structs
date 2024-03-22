import copy
from types import NoneType
from typing import Self

class AVL:
	def __init__(self, param: any = None):
		if type(param) in [int, NoneType]:
			self.node = param
			self.left = None
			self.right = None
			self.height = 1 if param else 0
		elif type(param) == AVL:
			# FIXME - PROBLEM IS HERE! Not truly passing by reference
			self.node = param.get_node()
			self.left = param.get_left()
			self.right = param.get_right()
			self.height = param.get_height()
		else: raise Exception("AVL must be initialized with either another AVL or an integer.")
		pass
	
	def get_node(self) -> int:
		return self.node
	
	def set_node(self, node):
		self.node = node

	def get_left(self) -> Self:
		return self.left
	
	def set_left(self, left):
		self.left = left

	def get_right(self) -> Self:
		return self.right
	
	def set_right(self, right):
		self.right = right

	def get_height(self) -> int:
		return self.height
	
	def set_height(self, height):
		self.height = height



	def balance(self, root: Self):
		if not root:
			return 0
		return root.get_left() - root.get_right()

	def rotate_right(self, old_root: Self):
		# Rotation right
		new_root = old_root.get_left()
		old_root.set_left(new_root.get_right())
		new_root.set_right(old_root)

		# Update heights of involved nodes
		old_root.set_height(max(AVL(old_root.get_left()), AVL(old_root.get_right())) + 1)
		new_root.set_height(max(AVL(new_root.get_left()), AVL(new_root.get_right())) + 1)
		return new_root

	def rotate_left(self, old_root: Self):
		# Rotate left
		new_root = old_root.get_right()
		old_root.set_right(new_root.get_left())
		new_root.set_left(old_root)

		# Update heights of involved nodes
		old_root.set_height(max(AVL(old_root.get_left()), AVL(old_root.get_right())) + 1)
		new_root.set_height(max(AVL(new_root.get_left()), AVL(new_root.get_right())) + 1)
		return new_root

	def _add(self, root: Self, node: int):
		if not root or not root.get_node():
			return AVL(node)
		if node < root.get_node():
			root.set_left(self._add(root.get_left(), node))
		else:
			root.set_right(self._add(root.get_right(), node))

		root.set_height(max(AVL(root.get_left()), AVL(root.get_right())) + 1)
		balance = self.balance(root)

		if balance > 1:
			if node < root.get_left().get_node():
				return self.rotate_right(root)
			else:
				root.set_left(self.rotate_left(root.get_left()))
				return self.rotate_right(root)
		if balance < -1:
			if node > root.get_right().get_node():
				return self.rotate_left(root)
			else:
				root.set_right(self.rotate_right(root.get_right()))
				return self.rotate_left(root)
		return root

	def add(self, node: int):
		root = self._add(self, node)
		self.set_node(root.get_node())
		self.set_left(root.get_left())
		self.set_right(root.get_right())
		self.set_height(root.get_height())

	
	def _pre_order(self, root: Self):
		if root:
			print(root.get_node())
			self._pre_order(root.get_left())
			self._pre_order(root.get_right())

	def traverse(self, algo: str = "preorder"):
		if algo == "preorder":
			self._pre_order(self)



	def __gt__(self, other: any):
		if type(other) == AVL:
			return (self.get_height() or 0) > (other.get_height() or 0)
		elif type(other) in [int, NoneType]:
			return (self.get_height() or 0) > (other or 0)

	def __lt__(self, other: Self):
		if type(other) == AVL:
			return (self.get_height() or 0) < (other.get_height() or 0)
		elif type(other) in [int, NoneType]:
			return (self.get_height() or 0) < (other or 0)
	
	'''
	Used in max(a: AVL, b: AVL)
	'''
	def __add__(self, other: Self):
		if type(other) == AVL:
			return (self.get_height() or 0) + (other.get_height() or 0)
		elif type(other) in [int, NoneType]:
			return (self.get_height() or 0) + (other or 0)
		
	def __sub__(self, other: Self):
		if type(other) == AVL:
			return (self.get_height() or 0) - (other.get_height() or 0)
		elif type(other) in [int, NoneType]:
			return (self.get_height() or 0) - (other or 0)

	def __rsub__(self, other: Self):
		if type(other) == AVL:
			return (other.get_height() or 0) - (self.get_height() or 0)
		elif type(other) in [int, NoneType]:
			return (other or 0) - (self.get_height() or 0)