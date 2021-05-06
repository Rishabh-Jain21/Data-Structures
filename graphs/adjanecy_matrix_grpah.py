class Graph:

    def __init__(self, vertices):
        self.adjMat = [[0 for i in range(vertices)] for j in range(vertices)]
        self.vertices = vertices

    def insert_edge(self, u, v, x=1):
        self.adjMat[u][v] = x

    def remove_edge(self, u, v):
        self.adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self.adjMat[u][v] != 0

    def vertex_count(self):
        return self.vertices

    def edge_count(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMat[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self.vertices):
            print(i, end=' ')
        print()

    def edges(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMat[i][j] != 0:
                    print(i, '--', j)

    def outdegree(self, v):
        count = 0
        for j in range(self.vertices):
            if not self.adjMat[v][j] == 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for j in range(self.vertices):
            if not self.adjMat[j][v] == 0:
                count += 1
        return count

    def display_adjMat(self):
        print(*self.adjMat, end="\n")

    def DFS(self, s):
        stack = []
        visited = [0]*self.vertices
        stack.append(s)
        print(s, end=" ")
        visited[s] = 1
        while(stack):
            i = stack.pop()
            for j in range(self.vertices):
                if self.adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end=" ")
                    visited[j] = 1
                    stack.append(j)

    def BFS(self, s):
        i = s
        queue = []
        visited = [0] * self.vertices
        print(i, end=' ')
        visited[i] = 1
        queue.append(i)

        while queue:
            i = queue.pop(0)
            for j in range(self.vertices):
                if self.adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end=' ')
                    visited[j] = 1
                    queue.append(j)


G = Graph(7)
G.insert_edge(0, 1)
G.insert_edge(0, 5)
G.insert_edge(0, 6)
G.insert_edge(1, 0)
G.insert_edge(1, 2)
G.insert_edge(1, 5)
G.insert_edge(1, 6)
G.insert_edge(2, 3)
G.insert_edge(2, 4)
G.insert_edge(2, 6)
G.insert_edge(3, 4)
G.insert_edge(4, 2)
G.insert_edge(4, 5)
G.insert_edge(5, 2)
G.insert_edge(5, 3)
G.insert_edge(6, 3)
G.display_adjMat()
G.DFS(0)
