class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for other_node in self.graph:
                self.graph[other_node] = [neighbor for neighbor in self.graph[other_node] if neighbor != node]

    def search_node(self, node):

        return node in self.graph

    def print_graph(self):
        for node in self.graph:
            neighbors = ", ".join(map(str, self.graph[node]))
            print(f"{node}: {neighbors}")

graph = Graph()

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

print("Graph after insertion:")
graph.print_graph()
print()
print("Is node 2 in the graph?", graph.search_node(2))
print()
graph.remove_node(3)

print("Graph after removing node 3:")
print()
graph.print_graph()
