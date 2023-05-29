class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = {}

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.add_vertex(start)
        if end not in self.graph:
            self.add_vertex(end)
        self.graph[start][end] = weight

    def listAdjacentVertex(self, vertex):
        if vertex in self.graph:
            for v in self.graph[vertex]:
                print(v)
        else:
            return "Vertex not found"

    def sumHighestAdjacentVertex(self, vertex):
        value = 0
        if vertex in self.graph:
            for v in self.graph[vertex]:
                value += self.graph[vertex][v]
            return value
        else:
            return value


# Graph 1
graph1 = Graph()
graph1.add_edge('A', 'B', 4)
graph1.add_edge('A', 'C', 2)
graph1.add_edge('B', 'C', 5)
graph1.add_edge('B', 'D', 10)
graph1.add_edge('C', 'E', 3)
graph1.add_edge('D', 'F', 11)
graph1.add_edge('E', 'D', 4)
print("Graph 1\nAdjacent vertices of A: ")
graph1.listAdjacentVertex('A')
print("Sum of weights for the vertex A:", graph1.sumHighestAdjacentVertex('A'))

# Graph 2
graph2 = Graph()
graph2.add_edge('G', 'H', 4)
graph2.add_edge('H', 'J', 4)
graph2.add_edge('I', 'H', 3)
graph2.add_edge('J', 'G', 3)
graph2.add_edge('J', 'I', 2)
graph2.add_edge('J', 'K', 3)
graph2.add_edge('K', 'H', 4)
graph2.add_edge('K', 'J', 5)
graph2.add_edge('K', 'L', 1)
graph2.add_edge('L', 'G', 5)
print("\nGraph 2\nAdjacent vertices of J: ")
graph2.listAdjacentVertex('J')
print("Sum of weights for the vertex J:", graph2.sumHighestAdjacentVertex('J'))
