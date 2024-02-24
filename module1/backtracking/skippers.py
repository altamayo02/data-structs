import copy

formation = [
    [-1, -1, -1, 0, 1, 1, 1],
]

moves = [-2, -1, 1, 2]

def is_valid(fmtn, pos):
    return 0 <= pos < len(fmtn)

def is_viable(fmtn):
    return fmtn != formation

def backtrack(fmtn: list, pos: int = 0, sln: list = []):
    if is_valid(fmtn, pos):
        print(fmtn, formation, fmtn == formation)
        if is_viable(fmtn):
            sln.append(copy.deepcopy(fmtn))
            # b r u h
            if fmtn == list.reverse(formation):
                print_sol(sln)
            else:
                for move in moves:
                    backtrack(fmtn, pos + move[0], sln)
            sln.pop()

def print_sol(sol):
    for fmtn in sol:
        for row in fmtn:
            print(row)
        print("---------------")