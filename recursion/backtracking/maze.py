import copy

class MazeSolver:
    def __init__(self, maze, moves, start: tuple):
        self.maze = maze
        self.moves = moves
        self.sln = []
        self.backtrack(self.maze, start[0], start[1])


    def is_valid(maze, row, col):
        return (
            0 <= row < len(maze) and
            0 <= col < len(maze[0])
        )

    def is_viable(maze, row, col):
        return maze[row][col] == 0

    def backtrack(self, maze: list, row: int = 0, col: int = 0):
        print(row, col)
        if self.is_valid(maze, row, col):
            if self.is_viable(maze, row, col):
                maze[row][col] = 2
                self.sln.append(copy.deepcopy(maze))
                if row == 4 and col == 4:
                    self.print_sln(self.sln)
                else:
                    for move in self.moves:
                        self.backtrack(maze, row + move[0], col + move[1])
                maze[row][col] = 0
                self.sln.pop()

    def print_sln(self):
        for maze in self.sln:
            for row in maze:
                print(row)
            print("---------------")

maze = MazeSolver(
    [
        [0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ],
    [
        (-1, 0), (0, -1), (0, 1), (1, 0)
    ],
    (0, 0)
)
maze.print_sln()