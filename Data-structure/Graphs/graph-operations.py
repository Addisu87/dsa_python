# Graph representation using adjacency list

class Graph:
   # constructor
   def __init__(self):
      self.adj_list = {}
      
   # a method to show a graph
   def print_graph(self):
      for vertex in self.adj_list:
         print(vertex, ':', self.adj_list[vertex])
         
   # Graph Add vertex
   def add_vertex(self, vertex):
      # Check if the vertex is not already in the graph
      if vertex not in self.adj_list.keys():
         # If the vertex is not already in the graph,
         # add it as a new key in the adj_list
         # with an empty list as it's value
         self.adj_list[vertex] = []
         # Return True to indicate that the vertex was successfully added to the graph
         return True
      # If the vertex is already in the graph, do not add it again
      # Return False to indicate that the vertex was not added to the graph
      return False
   
   # Graph Add edges
   def add_edge(self, v1, v2):
      # Check that both v1 and v2 are already in the graph
      if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
         # Add v2 to the adjacency list for v1 and vice versa
         self.adj_list[v1].append(v2)
         self.adj_list[v2].append(v1)
         # Return True to indicate that the edge was successfully added to the graph
         return True
      # If either v1 or v2 is not in the graph, do not add the edge
      # Return False to indicate that the edge was not added to the graph
      return False
   
   # Graph remove edge
   def remove_edge(self, v1, v2):
      # Check that both v1 and v2 are already in the graph
      if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
         try:
            # Attempt to remove v2 from the adjacency list of v1 and vice versa
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
         except ValueError:
            # If either v1 or v2 is not present in the adjacency list
            # of the other, catch the exception and do nothing
            pass
         # Return True to indicate that the edge was successfully removed from the graph 
         return True
      # If either v1 or v2 is not in the graph, do not attempt to remove the edge
      # Return False to indicate that the edge was not removed from the graph 
      return False
   
   # Graph remove vertex
   def remove_vertex(self, vertex):
      # Check if the vertex to be removed is in the adjacency list
      if vertex in self.adj_list.keys():
         # Loop over all vertices adjacent to the vertex to be removed
         for other_vertex in self.adj_list[vertex]:
            # Remove the vertex to be removed from the list of
            # adjacent vertices of the other vertices
            self.adj_list[other_vertex].remove(vertex)
            # After removing all the edges, 
            # remove the vertex from the adjacency list
         del self.adj_list[vertex]
         # Return True to indicate that the vertex was
         # successfully removed from the graph
         return True
      # If the vertex to be removed is not in the graph, return True
      return False
         
my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "D")

# print('Graph before remove_edge():')
# my_graph.print_graph()


# my_graph.remove_edge('A','C')


# print('\nGraph after remove_edge():')
# my_graph.print_graph()



print('Graph before remove_vertex():')
my_graph.print_graph()

my_graph.remove_vertex('D')

print('\nGraph after remove_vertex():')
my_graph.print_graph()
