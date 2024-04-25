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
g.traverse_girth('a')
print()
g.traverse_depth('a')

del g

g = NDGraph()
g.add(Point((2, 3)))
g.add(Point((5, 7)))
g.add(Point((5, 9)))
g.add(Point((4, 3)))
g.add(Point((11, 6)))
g.add(Point((1, 1)))