class Graph:
    def __init__(self):
        self.graph = {}

    def create_vertex(self, vertex):
        self.graph[vertex] = []

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex)
        for key, value in self.graph.items():
            if vertex in value:
                value.remove(vertex)

    def add_node(self, v1, v2=None, is_direct=False):
        if v1 and not isinstance(v1, bool):
            if v1 not in self.graph:
                self.create_vertex(v1)
            if v2 and not isinstance(v2, bool):
                if v2 not in self.graph:
                    self.create_vertex(v2)
                self.graph[v1].append(v2)
                if is_direct:
                    self.graph[v2].append(v1)
        elif v2 and not isinstance(v2, bool):
            if v2 not in self.graph:
                self.create_vertex(v2)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                neighbors_to_visit = [
                    neighbor for neighbor in self.graph[vertex]
                    if neighbor not in visited
                ]
                queue.extend(neighbors_to_visit)
        print()

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                neighbors_to_visit = [
                    neighbor for neighbor in self.graph[vertex]
                    if neighbor not in visited
                ]
                stack.extend(neighbors_to_visit)
        print()


graph = Graph()
graph.add_node("Mumbai", "Paris")
graph.add_node("Paris", "New York", True)
graph.add_node("Delhi", "Dubai", True)
graph.add_node("Dubai", "Paris", True)

graph.bfs("Dubai")
