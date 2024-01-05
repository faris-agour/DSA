class Graph:
    def __init__(self):
        self.adj_graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_graph.keys():
            self.adj_graph[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_graph.keys() or vertex2 in self.adj_graph.keys():
            self.adj_graph[vertex1].append(vertex2)
            self.adj_graph[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        try:
            if vertex1 in self.adj_graph.keys() or vertex2 in self.adj_graph.keys():
                self.adj_graph[vertex1].remove(vertex2)
                self.adj_graph[vertex2].remove(vertex1)
                return True
        except ValueError:
            pass
        return False

    def remove_vertex(self, vertex):
        try:
            if vertex in self.adj_graph.keys():
                for other_vertex in self.adj_graph[vertex]:
                    self.remove_edge(vertex, other_vertex)
                del self.adj_graph[vertex]
                return True
            return False
        except ValueError:
            pass

    def print_graph(self):
        for vertex in self.adj_graph.keys():
            print(f"{vertex} : {self.adj_graph[vertex]}")


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'D')
my_graph.add_edge('D', 'A')

my_graph.remove_edge('A', 'C')
my_graph.remove_edge('A', 'L')

my_graph.remove_vertex("D")
my_graph.remove_vertex("K")

my_graph.print_graph()
