from model.NDGraph import NDGraph
from model.Point import Point

g = NDGraph()
g.add('a')
g.add('b')
g.add('c')
g.add('d')
g.add('e')
g.connect('a', 'b', 10)
g.connect('a', 'c', 8)
g.connect('b', 'd', 11)
g.connect('b', 'e', 5)
g.connect('c', 'e', 3)

del g

g = NDGraph()
g.add(Point((2, 3)))
g.add(Point((5, 7)))
g.add(Point((5, 9)))
g.add(Point((4, 3)))
g.add(Point((11, 6)))
g.add(Point((1, 1)))

del g

g = NDGraph()
g.add('a')
g.add('b')
g.add('c')
g.add('d')
g.add('e')
g.add('f')
g.add('g')

g.connect('a', 'b', True)
g.connect('a', 'c', True)
g.connect('a', 'd', True)
g.connect('b', 'd', True)
g.connect('c', 'd', True)
g.connect('d', 'e', True)
g.connect('e', 'f', True)
g.connect('e', 'g', True)
g.connect('f', 'g', True)

for vertex in g.get_nodes():
    g.breadth_first_search(vertex)
    print()

del g

g = NDGraph()
for terminal in [
    10, 15, 20, 25,
    30, 35, 40, 45,
    47,
    50, 55, 60, 65
]:
    g.add(terminal)
g.connect(10, 15, 1)
g.connect(10, 30, 1)
g.connect(15, 20, 1)
g.connect(15, 35, 1)
g.connect(20, 25, 1)
g.connect(20, 40, 1)
g.connect(25, 45, 1)
g.connect(30, 47, 1)
g.connect(35, 40, 1)
g.connect(35, 55, 1)
g.connect(40, 60, 1)
g.connect(45, 65, 1)
g.connect(47, 50, 1)
g.connect(50, 55, 1)
g.connect(55, 60, 1)
g.connect(60, 65, 1)

dijkstra = {}
lifespan = 2

possible = []
for terminal in dijkstra:
    if dijkstra[terminal] <= lifespan:
        possible.append(terminal)

g = NDGraph()
g.add('A')
g.add('B')
g.add('C')
g.add('D')
g.add('E')
g.add('F')
g.add('G')
g.add('H')

g.connect('A', 'B', 9)
g.connect('A', 'C', 5)
g.connect('A', 'D', 6)
g.connect('B', 'C', 7)
g.connect('B', 'D', 3)
g.connect('B', 'E', 5)
g.connect('C', 'E', 2)
g.connect('C', 'F', 2)
g.connect('D', 'E', 1)
g.connect('D', 'G', 4)
g.connect('E', 'F', 7)
g.connect('E', 'G', 5)
g.connect('E', 'H', 1)
g.connect('F', 'H', 3)
g.connect('F', 'G', 9)

g.breadth_first_search('A')
g.depth_first_search('A')
g.dijkstra('A')
g.floyd_warshall()

del g

