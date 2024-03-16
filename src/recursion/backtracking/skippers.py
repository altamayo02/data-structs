import copy

class Skippers:
	def __init__(self, formation):
		self.moves = [-2, -1, 1, 2]
		self.formation = formation
	
	def is_valid(self, fmtn, pos):
		return 0 <= pos[0] < len(fmtn)

	def is_viable(self, fmtn):
		indices = range(len(self.formation))
		return zip(indices, fmtn) != zip(indices, self.formation)

	def backtrack(self, fmtn: list = None, pos: tuple = (3, 3), sln: list = [], first: bool = False):
		if not fmtn:
			fmtn = self.formation
		if self.is_valid(fmtn, pos):
			if self.is_viable(fmtn) or first:
				# TODO - Keep track of already visited states
				fmtn[pos[0]], fmtn[pos[1]] = fmtn[pos[1]], fmtn[pos[0]]
				sln.append(copy.deepcopy(fmtn))
				if fmtn == reversed(self.formation):
					self.print_sol(sln)
				else:
					for move in self.moves:
						self.backtrack(fmtn, (pos[0] + move, pos[0]), sln)
				sln.pop()
				print(20 * "-")


	def print_sol(self, sol):
		for fmtn in sol:
			for row in fmtn:
				print(row)
			print("---------------")

	def exec(self):
		self.backtrack(first = True)

formation = [
    [-1, -1, -1, 0, 1, 1, 1],
]

moves = [-2, -1, 1, 2]