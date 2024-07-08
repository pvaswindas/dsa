class Graph:
    def __init__(self):
        self.graph = {}

    def create_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edges(self, edges, is_direct=False):
        for start, end in edges:
            if start and end:
                if start not in self.graph:
                    self.create_vertex(start)
                if end not in self.graph:
                    self.create_vertex(end)
                self.graph[start].append(end)
                if is_direct:
                    self.graph[end].append(start)
            elif start:
                if start not in self.graph:
                    self.create_vertex(start)

    def display_all(self):
        print(self.graph)

    def add_node(self, vertex1, vertex2=None, is_direct=False):
        if vertex1 and not isinstance(vertex1, bool):
            if vertex1 not in self.graph:
                self.create_vertex(vertex1)
            if vertex2 and not isinstance(vertex2, bool):
                if vertex2 not in self.graph:
                    self.create_vertex(vertex2)
                self.graph[vertex1].append(vertex2)
                if is_direct:
                    self.graph[vertex2].append(vertex1)
        elif vertex2:
            if vertex2 not in self.graph:
                self.create_vertex(vertex2)
                self.create_vertex(vertex2)


routes = [
    ("Mumbai", "Paris"),
    ("New York", "Paris"),
    ("Mumbai", "New York"),
]
graph = Graph()
graph.add_node("Mumbai", "Paris")

graph.display_all()
