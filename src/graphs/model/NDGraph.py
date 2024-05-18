from collections import deque

#Dijkstra, Floyd-Warshall, Bellman-Ford
#Prim, Kruskal, Vorubka

class NDGraph:
    def __init__(self):
        self.nodes: dict[any, dict[any, any]] = {}
    
    def get_nodes(self):
        return self.nodes
    
    def get_shallow_nodes(self):
        return list(self.nodes.keys())

    def get_adjacents(self, vertex):
        return list(self.nodes[vertex].keys())

    def add(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = {}
    
    def connect(self, v1, v2, weight = None):
        if v1 in self.nodes and v2 in self.nodes:
            self.nodes[v1][v2], self.nodes[v2][v1] = weight, weight
    
    def breadth_first_search(self, origin):
        queue = deque([origin])
        # Conjunto: Colección de elementos únicos
        traversed = set()
        traversal = []
        while queue:
            node = queue.popleft()
            traversal.append(node)
            traversed.add(node)
            for adj in self.get_adjacents(node):
                if adj not in queue and adj not in traversed:
                    # Encolar
                    queue.append(adj)
        
        return traversal
    
    def depth_first_search(self, origin):
        stack = [origin]
        traversed = set()
        traversal = []
        while stack:
            node = stack.pop()
            traversal.append(node)
            traversed.add(node)
            for adj in self.get_adjacents(node):
                if adj not in stack and adj not in traversed:
                    # Apilar
                    stack.append(adj)
        
        return traversal

    def dijkstra(self, origin):
        queue = [(0, origin)]
        traversed = set()
        distances = {node: float('inf') for node in self.nodes}
        distances[origin] = 0
        while queue:
            curr_dist, node = min(queue)
            queue.remove((curr_dist, node))
            if node not in traversed:
                traversed.add(node)
                for adj, dist_to_adj in self.nodes[node].items():
                    new_dist = curr_dist + dist_to_adj
                    if new_dist < distances[adj]:
                        distances[adj] = new_dist
                        queue.append((new_dist, adj))
        return distances

    def floyd_warshall(self):
        distances = {
            n1: {n2: float('inf') for n2 in self.nodes} for n1 in self.nodes
        }
        for node in self.nodes:
            distances[node][node] = 0
            for adj in self.get_adjacents(node):
                distances[node][adj] = self.nodes[node][adj]
        for k in self.nodes:
            for i in self.nodes:
                for j in self.nodes:
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        return distances

    """ def bellman_ford(self, origin):
        distances = {node: float('inf') for node in self.nodes}
        distances[origin] = 0

        for _ in range(len(distances) - 1):
            for i in range(len(distances)):
                for j in range(len(distances)):
                    if (
                        distances[i][j] != 0 and
                        distances[i]
                    ):
                        pass """
