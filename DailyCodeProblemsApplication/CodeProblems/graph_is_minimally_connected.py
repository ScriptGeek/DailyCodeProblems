"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as either an adjacency matrix or adjacency list.

Upgrade to premium and get in-depth solutions to every problem, including this one. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

Ready to interview? Take Triplebyte's quiz and skip straight to final interviews with top tech companies!
"""





"""
ScriptGeek's solution:

An adjacency list is used to represent the graph.
A test graph is constructed and a method called is_minimally_constructed determines the 
result of the graph.

The secret to getting the correct answer without developing a complex solution is 2 facts:
1. A minimally connected graph has n-1 connections where n is the number of nodes
(in the graph to be tested has 2x the number of connections due to being undirected, so
this number must be divided in half and then subtract 1 when checking)
2. Every node must have at least one connection

"""

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.connections = []

    def get_link_count(self):
        count = 0
        return len(self.connections)


# A class to represent a graph. A graph is the list of adjacency lists.
# Size of the array will be the number of vertices.
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * vertices

    # Method to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        
        srcNode = self.graph[src];
        if (srcNode == None):
            srcNode = AdjNode(src)
            self.graph[src] = srcNode

        destNode = self.graph[dest]
        if (destNode == None):
            destNode = AdjNode(dest)
            self.graph[dest] = destNode

        srcNode.connections.append(dest)
        destNode.connections.append(src)


    # Method to print the graph
    def print_graph(self):
        for i in range(self.vertices):
            print ("Adjacency list of vertex {}\n head".format(i), end="")
            node = self.graph[i]
            for connection in range(0,len(node.connections)):
                print(" -> {}".format(node.connections[connection]), end="")
            print(" \n")


    def is_minimally_connected(self):
        result = True
        total_connections = 0
        # The minimum total number of connections is one less than the number of vertices
        # (but this is undirected, so it must have 2x the number of connections).
        # The number of connections per node must be at least one.
        for v in range(0,self.vertices):
            connection_count = len(self.graph[v].connections)
            total_connections += connection_count
            if (connection_count < 1):
                result = False
                break

        print (f"connections: {total_connections} vertices: {self.vertices}")
        if (total_connections / 2 != self.vertices - 1):
            result = False
        return result



vertices = 5
graph = Graph(vertices)
graph.add_edge(0,1)
#    graph.add_edge(0,4)
graph.add_edge(1,2)
#    graph.add_edge(1,3)
#    graph.add_edge(1,4)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.print_graph()

NOT = "IS "
if (not graph.is_minimally_connected()):
    NOT = "IS NOT "
print (f"graph {NOT}minimally connected");

#    for v in range(0,graph.vertices):
#        links = graph.graph[v].get_link_count()
#        print (f"vertex: {v} -> links: {links}")


"""

Minimally connected graph:

1. Every node must have at least one connection.
2. Removing any connection causes a node to become disconnected.
3. Minimally connected graph is a tree; therefore, the number of connections is one less the number of nodes

So:
    Every node must have at least one connection.
    The number of connections is one less the number of nodes.

"""