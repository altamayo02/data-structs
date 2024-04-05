from collections import deque

class NDGraph:
    def __init__(self):
        self.vertices: dict[any, dict[any, any]] = {}
    
    def add(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}
    
    def connect(self, v1, v2, weight):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][v2], self.vertices[v2][v1] = weight, weight
    
    def get_vertices(self):
        return list(self.vertices.keys())

    def get_adjacents_of(self, vertex):
        return list(self.vertices[vertex].keys())
    
    def traverse_girth(self, origin):
        queue = deque([origin])
        # Conjunto: Colección de elementos únicos
        traversed = set()

        while queue:
            elem = queue.popleft()
            print(elem, end='-')
            traversed.add(elem)
            for adj in self.get_adjacents_of(elem):
                if adj not in queue and adj not in traversed:
                    # Encolar
                    queue.append(adj)
    
    def traverse_depth(self, origin):
        stack = [origin]
        traversed = set()
        
        while stack:
            elem = stack.pop()
            print(elem, end='-')
            traversed.add(elem)
            for adj in self.get_adjacents_of(elem):
                if adj not in stack and adj not in traversed:
                    # Apilar
                    stack.append(adj)