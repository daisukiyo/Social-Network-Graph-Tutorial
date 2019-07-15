#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # TODO check if vertex is already a neighbor
        # TODO if not, add vertex to neighbors and assign weight.
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
            

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        # TODO return the neighbors
        return self.neighbors

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        # TODO return the weight of the edge from this vertext to the given vertex.
        return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # TODO increment the number of vertices
        # TODO create a new vertex
        # TODO add the new vertex to the vertex list
        # TODO return the new vertex
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex


    def getVertex(self, key):
        """return the vertex if it exists"""
        # TODO return the vertex if it is in the graph
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Tim")
    g.addVertex("Ryan")
    g.addVertex("Cenz")
    g.addVertex("Tom")
    g.addVertex("Austyn")
    g.addVertex("Shu")
    g.addVertex("Bryan")
    g.addVertex("Aleck")
    g.addVertex("Tommy")


    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Tim", "Ryan")
    g.addEdge("Tim", "Cenz")
    g.addEdge("Tim", "Tom")
    g.addEdge("Tim", "Austyn")
    g.addEdge("Tim", "Shu")
    g.addEdge("Tim", "Bryan")
    g.addEdge("Tim", "Aleck")
    g.addEdge("Tim", "Tommy")
    
    g.addEdge("Austyn", "Shu")
    g.addEdge("Austyn", "Bryan")
    g.addEdge("Austyn", "Aleck")
    g.addEdge("Austyn", "Tommy")

    g.addEdge("Ryan", "Cenz")
    g.addEdge("Ryan", "Tom")
    g.addEdge("Ryan", "Austyn")

    g.addEdge("Cenz", "Tom")

    g.addEdge("Tom", "Tommy")

    g.addEdge("Shu", "Bryan")
    
    g.addEdge("Bryan", "Aleck")

    g.addEdge("Aleck", "Tommy")


    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
