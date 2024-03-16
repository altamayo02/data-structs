from maze import MazeSolver

class Cheese(MazeSolver):
    pass

test = Cheese(
    [
        [0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ],
    [
        (-1, 0), (0, -1), (0, 1), (1, 0)
    ]
)
test.print_sln()