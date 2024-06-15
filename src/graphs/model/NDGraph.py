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

	def get_adjacents(self, node):
		return self.nodes[node].items()

	def get_shallow_adjacents(self, node):
		return list(self.nodes[node].keys())

	def add(self, node):
		if node not in self.nodes:
			self.nodes[node] = {}
	
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
			for adj in self.get_shallow_adjacents(node):
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
			for adj in self.get_shallow_adjacents(node):
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
				for adj, dist_to_adj in self.get_adjacents(node):
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
			for adj in self.get_shallow_adjacents(node):
				distances[node][adj] = self.nodes[node][adj]
		for k in self.nodes:
			for i in self.nodes:
				for j in self.nodes:
					distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
		return distances

	def bellman_ford(self, origin):
		distances = {node: float('inf') for node in self.nodes}
		distances[origin] = 0

		for _ in range(len(distances) - 1):
			for node in self.nodes:
				for adj, dist_to_adj in self.get_adjacents(node):
					new_dist = distances[node] + dist_to_adj
					if new_dist < distances[adj]:
						distances[adj] = new_dist
		return distances
	
	def primm(self, origin):
		candidates = []
		for adj, dist_to_adj in self.get_adjacents(origin):
			candidates.append((dist_to_adj, origin, adj))
		
		traversed = set()
		traversed.add(origin)
		min_span_tree = []
		while candidates:
			candidates.sort()
			distance, start, end = candidates.pop(0)

			if end not in traversed:
				traversed.add(end)
				min_span_tree.append((start, end, distance))

				for adj, dist_to_adj in self.get_adjacents(end):
					if adj not in traversed:
						candidates.append((dist_to_adj, end, adj))
		return min_span_tree
	
	def kruskal(self):
		edges = []
		for start in self.nodes:
			for end, distance in self.get_adjacents(start):
				edges.append((distance, start, end))
		edges.sort()

		sets = [{node} for node in self.nodes]
		min_span_tree = []
		for distance, start, end in edges:
			start_set = None
			end_set = None

			for set in sets:
				if start in set:
					start_set = set
				if end in set:
					end_set = set

			if start_set != end_set:
				min_span_tree.append((start, end, distance))
				start_set.update(end_set)
				sets.remove(end_set)
		return min_span_tree
	
	# https://www.geeksforgeeks.org/boruvkas-mst-in-python/
	""" def boruvka(self):
		ranks = []
		parent_tree = []
		for node in self.nodes:
			parent_tree.append(node)
			ranks.append(0)

		shortest = [-1 for _ in self.nodes]
		num_trees = len(self.nodes)
		while num_trees > 1:
			for i in range(len()) """