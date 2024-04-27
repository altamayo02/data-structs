from typing import Self


class BinaryTree:
	def __init__(self, root = None, left: Self = None, right: Self = None):
		self.root = root
		self.left = left
		self.right = right
	
	def get_root(self) -> any:
		from model.Soccer import SoccerTeam
		if type(self.root) is SoccerTeam:
			return self.root.to_dict()
		return self.root
	
	def get_left(self) -> Self:
		return self.left

	def get_right(self) -> Self:
		return self.right
	
	def set_root(self, root):
		self.root = root

	def set_left(self, left):
		self.left = left

	def set_right(self, right):
		self.right = right
	
	def in_order(self, root: Self, f = None):
		if root:
			if not f:
				f = root.get_root
			return (
				self.in_order(root.get_left()) +
				[f()] +
				self.in_order(root.get_right())
			)
		return []
		
	def pre_order(self, root: Self, f = None):
		if root:
			if not f:
				f = root.get_root
			return (
				[f()] +
				self.pre_order(root.get_left()) +
				self.pre_order(root.get_right())
			)
		return []

	def post_order(self, root: Self, f = None):
		if root:
			if not f:
				f = root.get_root
			return (
				self.post_order(root.get_left()) +
				self.post_order(root.get_right()) +
				[f()]
			)
		return []
		
	def height(self, root: Self):
		if root:
			return max(
				self.height(root.get_left()) + 1,
				self.height(root.get_right()) + 1
			)
		return 0

	def weight(self, root: Self):
		if root:
			return 1 + (
				self.weight(root.get_left()) +
				self.weight(root.get_right())
			)
		return 0

	def min(self, root: Self):
		if root:
			if not root.get_left():
				return root.get_root()
			return self.min(root.get_left())
		return None

	def max(self, root: Self):
		if root:
			if not root.get_right():
				return root.get_root()
			return self.max(root.get_right())
		return None

	def balance(self, root):
		if root:
			return
		else:
			return 0

	def levels(self, root: Self):
		queue = [root]
		while queue:
			first = queue.pop(0)
			print(first.get_root())
			if first.get_left():
				queue.append(first.get_left())
			if first.get_right():
				queue.append(first.get_left())

	def branch(self, root: Self):
		# This is private!!! Encapsulation!!!
		# Cierra el goteo (?)
		def visit_branch(root: Self, branch: list, branches: list):
			if not root:
				return
			branch.append(root.get_root())
			if not root.get_left() and not root.get_right():
				branches.append(branch.copy())
			else:
				visit_branch(root.get_left(), branch, branches)
				visit_branch(root.get_right(), branch, branches)
			branch.pop()
		return visit_branch(root, [], [])

	# Habitual - Por la derecha
	def remove_node(self, root: Self, value):
		if root:
			if value < root.get_root():
				root.set_left(self.remove_node(root.get_left(), value))
			elif value > root.get_root():
				root.set_right(self.remove_node(root.get_right(), value))
			else:
				if not root.get_left():
					return root.get_right()
				elif not root.get_left():
					return root.get_right()
				else:
					root.set_root(self.min(root.get_right()))
					root.set_right(self.remove_node(root.get_right(), root.get_root()))
		else:
			return None

	def to_dict(self, root: Self = None) -> dict:
		if self.root:
			if not root:
				root = self.root
			return {
				"root": root.get_root() if root else None,
				"left": self.to_dict(root.get_left()) if root.get_left() else None,
				"right": self.to_dict(root.get_right()) if root.get_right() else None
			}