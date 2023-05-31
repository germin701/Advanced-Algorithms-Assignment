class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = {}

    def add_edge(self, start, end, weight):
        # Add vertex if not exist
        if start not in self.graph:
            self.add_vertex(start)
        # Add vertex if not exist
        if end not in self.graph:
            self.add_vertex(end)
        # Add weight to the dictionary
        self.graph[start][end] = weight

    def print(self):
        for start in self.graph:
            for end, weight in self.graph[start].items():
                print(start, "-", weight, "->", end)

    def listAdjacentVertex(self, vertex):
        # Verify the vertex is existed or not
        if vertex in self.graph:
            # Verify the vertex has adjacent vertex or not
            if self.graph[vertex]:
                # Print the key in the dictionary which are adjacent of the vertex
                for v in self.graph[vertex]:
                    print(v)
            else:
                print("None")
        else:
            return "Vertex not found"

    def sumHighestAdjacentVertex(self, vertex):
        # The sum of weight
        value = 0
        # Verify the vertex is existed or not
        if vertex in self.graph:
            # Sum up the value in the dictionary which are the weight of the adjacent vertex
            for v in self.graph[vertex]:
                value += self.graph[vertex][v]
            return value
        else:
            return value

    def print_adjacent_details(self):
        # Loop through all the vertex to print out their adjacent vertices and the sum of their adjacent vertices
        for vertex in self.graph:
            print("\nAdjacent vertices of", str(vertex), ": ")
            self.listAdjacentVertex(vertex)
            print("Sum of weights of the adjacent vertices of", str(vertex), ":",
                  self.sumHighestAdjacentVertex(vertex))

# Graph 1
graph1 = Graph()
graph1.add_edge('A', 'B', 4)
graph1.add_edge('A', 'C', 2)
graph1.add_edge('B', 'C', 5)
graph1.add_edge('B', 'D', 10)
graph1.add_edge('C', 'E', 3)
graph1.add_edge('D', 'F', 11)
graph1.add_edge('E', 'D', 4)
print("Graph 1")
graph1.print()
graph1.print_adjacent_details()

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
print("\nGraph 2")
graph2.print()
graph2.print_adjacent_details()
