import copy


table = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

def is_valid(table, row, col):
    return (
        0 <= row < len(table) and
        0 <= col < len(table[0])
    )

def is_viable(table, row, col):
    return table[row][col] == 0

def backtrack(table: list, row: int = 0, col: int = 0, sol: list = []):
    if is_valid(table, row, col):
        if is_viable(table, row, col):
            table[row][col] = len(sol) + 1
            sol.append(copy.deepcopy(table))
            '''
            This is another problem!
            if row == 2 and col == 3:
            '''
            '''
            Too CPU intensive!
            if all([all(v != 0 for v in row) for row in table]):
            '''
            if len(sol) == 12:
                print_sol(sol)
            else:
                for move in moves:
                    backtrack(table, row + move[0], col + move[1], sol)
            table[row][col] = 0
            sol.pop()

def print_sol(sol):
    for table in sol:
        for row in table:
            print(row)
        print("---------------")
    print("---------------")
    print("---------------")