import math
import datetime
from PIL import Image

RED = "\u001b[31m"
DEFAULT = "\u001b[0m"

mat = []
#SIZE = 64
SIZE = 996

for i in range(SIZE):
    mat.append([])
    for _ in range(SIZE):
        mat[i].append(0)

moves = [
    (0, 1), (1, 1)
]

def is_valid(K, n1, n2):
    return math.dist([0, 0], [n1, n2]) <= K * math.sqrt(3)

def is_viable(sln, n1, n2):
    return sln[n1 - 1][n2 - 1] == 0

# K = 35
def backtrack(sln: list, K: int =  570, n1: int = 1, n2: int = 1):
    if is_valid(K, n1, n2):
        if is_viable(sln, n1, n2):
            sln[n1 - 1][n2 - 1] = 1
            dist = math.dist([0, 0], [n1, n2])
            if 987.26 < round(dist, 4):
                print(f"({n1**2}, {n2**2}): {dist == K * math.sqrt(3)} ({dist})")
            if dist == K * math.sqrt(3):
                return dist
            else:
                for move in moves:
                    backtrack(sln, K, n1 + move[0], n2 + move[1])
            #print("---------------")
        #print("---------------")

def exec():
    backtrack(mat)
    #print_matrix(mat)
    print("***************")
    date = datetime.datetime.now()
    img = Image.new(mode = "RGB", size = (SIZE, SIZE))
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col]:
                img.putpixel((row + 1, col + 1), (255, 255, 255))
    img.save(f"./{date}.png")
    print("Image saved.")
    

def to_string(m):
    string = ""
    for row in m:
        for num in row:
            string += f"{num};"
            #string += f"{RED if num == 1 else ''}{num}{DEFAULT if num == 1 else ''} "
        string += "\n"
    return string