import copy

maze = [
    [0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

moves = [
    (-1, 0), (0, -1), (0, 1), (1, 0)
]

def is_valid(maze, row, col):
    return (
        0 <= row < len(maze) and
        0 <= col < len(maze[0])
    )

def is_viable(maze, row, col):
    return maze[row][col] == 0

def backtrack(maze: list, row: int = 0, col: int = 0, sol: list = []):
    if is_valid(maze, row, col):
        if is_viable(maze, row, col):
            maze[row][col] = 2
            sol.append(copy.deepcopy(maze))
            if row == 4 and col == 4:
                print_sol(sol)
            else:
                for move in moves:
                    backtrack(maze, row + move[0], col + move[1], sol)
            maze[row][col] = 0
            sol.pop()

def print_sol(sol):
    for maze in sol:
        for row in maze:
            print(row)
        print("---------------")