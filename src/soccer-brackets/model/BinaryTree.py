from typing import Self

class Node:
	def __init__(self, value, left: Self = None, right: Self = None) -> None:
		self.value = value
		self.left = left
		self.right = right

	def get_value(self):
		from model.Soccer import SoccerTeam
		if type(self.value) is SoccerTeam:
			return self.value.to_dict()
		return self.value

	def get_left(self) -> Self:
		return self.left

	def get_right(self) -> Self:
		return self.right
	
	def set_node(self, node):
		self.node = node
	
	def set_left(self, left):
		self.left = left

	def set_right(self, right):
		self.right = right


class BinaryTree:
	def __init__(self, root = None):
		self.root = root
		if type(root) is not Node:
			self.root = Node(root)
		else:
			self.root = root
	
	def get_root(self) -> any:
		return self.root
	
	def set_root(self, root):
		self.root = root
	
	def in_order(self, root: Node):
		if root:
			return (
				self.in_order(root.get_left()) +
				[root.get_value()] +
				self.in_order(root.get_right())
			)
		return []
		
	def pre_order(self, root: Node):
		if root:
			return (
				[root.get_value()] +
				self.pre_order(root.get_left()) +
				self.pre_order(root.get_right())
			)
		return []

	def post_order(self, root: Node):
		if root:
			return (
				self.post_order(root.get_left()) +
				self.post_order(root.get_right()) +
				[root.get_value()]
			)
		return []
		
	def height(self, root: Node):
		if root:
			return max(
				self.height(root.get_left()) + 1,
				self.height(root.get_right()) + 1
			)
		return 0

	def weight(self, root: Node):
		if root:
			return 1 + (
				self.weight(root.get_left()) +
				self.weight(root.get_right())
			)
		return 0

	def min(self, root: Node):
		if root:
			if not root.get_left():
				return root.get_value()
			return self.min(root.get_left())
		return None

	def max(self, root: Node):
		if root:
			if not root.get_right():
				return root.get_value()
			return self.max(root.get_right())
		return None

	# def balance(self, root):
	#     if root:
	#         return
	#     else:
	#         return 0

	def levels(self, root: Node):
		queue = [root]
		while queue:
			first = queue.pop(0)
			print(first.get_value())
			if first.get_left():
				queue.append(first.get_left())
			if first.get_right():
				queue.append(first.get_left())

	def branch(self, root: Node):
		# This is private!!! Encapsulation!!!
		# Cierra el goteo (?)
		def visit_branch(root: Node, branch: list, branches: list):
			if not root:
				return
			branch.append(root.get_value())
			if not root.get_left() and not root.get_right():
				branches.append(branch.copy())
			else:
				visit_branch(root.get_left(), branch, branches)
				visit_branch(root.get_right(), branch, branches)
			branch.pop()
		return visit_branch(root, [], [])

	# Habitual - Por la derecha
	def remove_node(self, root: Node, value):
		if root:
			if value < root.get_value():
				root.set_left(self.remove_node(root.get_left(), value))
			elif value > root.get_value():
				root.set_right(self.remove_node(root.get_right(), value))
			else:
				if not root.get_left():
					return root.get_right()
				elif not root.get_left():
					return root.get_right()
				else:
					root.set_node(self.min(root.get_right()))
					root.set_right(self.remove_node(root.get_right(), root.get_value()))
		else:
			return None

	def to_dict(self, root: Node = None) -> dict:
		if not root:
			root = self.root
		return {
			"root": root.get_value(),
			"left": self.to_dict(root.get_left()) if root.get_left() else None,
			"right": self.to_dict(root.get_right()) if root.get_right() else None
		}