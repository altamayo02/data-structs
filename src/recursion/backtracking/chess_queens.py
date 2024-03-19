import copy

class QueenSpawner():
	def __init__(self, table, moves):
		self.table = table
		self.moves = moves
		self.visits = []
		for row in range(len(table)):
			self.visits.append(len(table[row]) * [0])
		self.sln = []
		self.backtrack(self.table)

	def is_valid(self, table, row, col):
		return (
			0 <= row < len(table) and
			0 <= col < len(table[0])
		)
	
	def is_viable(self, table, row, col):
		return table[row][col] == 0

	def is_viable_move(self, table: list, row: int, col: int, move: tuple):
		if self.is_valid(table, row, col):
			if self.is_viable(table, row, col):
				return self.is_viable_move(table, row + move[0], col + move[1], move)
			return False
		return True

	def is_visited(self, row, col):
		return self.visits[row][col] != 0

	def backtrack(self, table: list, row: int = 0, col: int = 0, sln: list = []):
		if self.is_valid(table, row, col):
			if not self.is_visited(row, col):
				is_viable = True
				for move in self.moves:
					is_viable = is_viable and self.is_viable_move(table, row, col, move)
				if is_viable:
					table[row][col] = len(sln) + 1
					sln.append(copy.deepcopy(table))
					for r in sln[-1]:
						print(r)
					print("------------------")
					if len(sln) == len(table):
						print("done")
						self.sln = copy.deepcopy(sln)
				self.visits[row][col] = 1

				for move in self.moves:
					self.backtrack(table, row + move[0], col + move[1], sln)

	def __str__(self):
		s = ""
		for table in self.sln:
			for row in table:
				s += f"{row}\n"
			s += "---------------\n"
		s += "---------------\n---------------\n"
		return s

queens = QueenSpawner(
	table = [
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
	],
	moves = [
		(-1, -1), (-1, 0), (-1, 1),
		(0, -1), (0, 1),
		(1, -1), (1, 0), (1, 1)
	]
)

print(queens)