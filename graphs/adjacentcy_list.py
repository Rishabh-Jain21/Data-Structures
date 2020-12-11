class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight=1):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return f'{self.id} connected to {[x.id for x in self.connectedTo]}'


class Graph(object):
    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = +1
        newVertex = Vertex(key)
        self.verList[key] = newVertex
        return newVertex

    def getVertext(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def addEdge(self, f, t, cost=1):
        if f not in self.verList:
            nv = self.addVertex(f)
        if t not in self.verList:
            nv = self.addVertex(t)

        self.verList[f].addNeighbour(self.verList[t], cost)

    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

    def __contains__(self, n):
        return n in self.verList


g = Graph()


for i in range(1, 6):
    g.addVertex(i)
print(g.verList)
g.addEdge(1, 2)
g.addEdge(1, 4)
g.addEdge(3, 1)
g.addEdge(3, 4)
g.addEdge(4, 2)
g.addEdge(5, 4)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)


for vertex in g:
    print(vertex)
    print(vertex.getConnections())
