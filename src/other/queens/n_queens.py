import copy
from typing import Self


class Board:
	def __init__(self, matrix: list[list]):
		self.matrix = copy.deepcopy(matrix)

	def __eq__(self, other: Self):
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[i])):
				if self.matrix[i][j] != other.matrix[i][j]: return False
		return True
	
	def __str__(self):
		string = ""
		for i in range(len(self.matrix)):
			string += f'{" ".join(self.matrix[i])}\n'
		return string

def rotate(board):
	board: Board = board

	rotated: list[list] = []
	for row in range(len(board.matrix)):
		rotated.append([])
	for row in range(len(board.matrix)):
		for col in range(len(board.matrix)):
			rotated[len(board.matrix) - 1 - col].append(board.matrix[row][col])
	return Board(rotated)

def mirror(board):
	board: Board = board

	mirrored: list[list] = []
	for row in range(len(board.matrix)):
		mirrored.append([])
		for col in range(len(board.matrix)):
			mirrored[row].append(board.matrix[row][len(board.matrix) - 1 - col])
	return Board(mirrored)

# Thanks cmc!
# https://leetcode.com/problems/n-queens/solutions/19810/fast-short-and-easy-to-understand-python-solution-11-lines-76ms
def solve_n_queens(n):
	def DFS(queens, xy_dif, xy_sum):
		p = len(queens)
		if p==n:
			result.append(queens)
			return None
		for q in range(n):
			if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
				DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
	result = []
	DFS([],[],[])
	return [ [". "*i + "Q" + " ."*(n-i-1) for i in sol] for sol in result]

def read_n_queens(path: str):
	list_boards: list[Board] = []
	with open(path, 'r') as file:
		string = file.read()
		str_boards = string.split("-----------------------------\n")
		for b in range(len(str_boards)):
			list_boards.append(Board([]))

			rows = str_boards[b].split("\n")[:-1:]
			for r in range(len(rows)):
				list_boards[b].matrix.append([])

				cols = rows[r].split(" ")
				for c in cols:
					list_boards[b].matrix[r].append(c)
	return list_boards

def fundamentals(boards):
	boards: list[Board] = boards

	fundamentals: list[Board] = []
	percentage = 0
	for b1 in boards:
		print(f"{100 * percentage / len(boards):.2f}%")
		if b1 not in fundamentals:
			fundamentals.append(b1)
		for b2 in boards:
			same = False
			for _ in range(4):
				same = b2 == b1 or mirror(b2) == b1
				b2 = rotate(b2)
			if not same:
				fundamentals.append(b2)
		percentage += 1

boards = read_n_queens('./src/other/queens/n_queens.md')
# TODO - Prints NONE, should print a list of 46 items
print(fundamentals(boards))