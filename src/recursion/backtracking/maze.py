import copy

class MazeSolver:
	def __init__(self, maze, moves, start: tuple = (0, 0), end: tuple = (None)):
		self.maze = maze
		self.moves = moves
		self.sln = []
		if end == (None): end = (len(self.maze) - 1, len(self.maze[0]) - 1)
		self.end = end
		self.backtrack(self.maze, start[0], start[1])


	def is_valid(self, maze, row, col):
		return (
			0 <= row < len(maze) and
			0 <= col < len(maze[0])
		)

	def is_viable(self, maze, row, col):
		return maze[row][col] == 0

	def backtrack(self, maze: list, row: int = 0, col: int = 0, sln: list = []):
		if (row, col) == self.end:
			maze[row][col] = 2
			sln.append(copy.deepcopy(maze))
			self.sln = copy.deepcopy(sln)
			return
		for move in self.moves:
			if self.is_valid(maze, row, col):
				if self.is_viable(maze, row, col):
					maze[row][col] = 2
					sln.append(copy.deepcopy(maze))
					self.backtrack(maze, row + move[0], col + move[1])
					maze[row][col] = 0
					sln.pop()

	def __str__(self):
		s = ""
		for maze in self.sln:
			for row in maze:
				s += f"{row}\n"
			s += "---------------\n"
		return s