class Vertex:
    def __init__(self, key):
        self.mKey = key
        self.in_degree = 0
        self.out_degree = 0


class Graph:
    def __init__(self, n):
        self.mVertices = {i: Vertex(i) for i in range(1, n + 1)}

    def addEdge(self, u, v):
        if u in self.mVertices and v in self.mVertices:
            self.mVertices[u].out_degree += 1
            self.mVertices[v].in_degree += 1


if __name__ == "__main__":
    f = open("input.txt", "r")

    line = f.readline().split()
    if line:
        n = int(line[0])
        m = int(line[1])

        g = Graph(n)

        for _ in range(m):
            edge_line = f.readline().split()
            if edge_line:
                u = int(edge_line[0])
                v = int(edge_line[1])
                g.addEdge(u, v)

    f.close()

    for i in range(1, n + 1):
        v = g.mVertices[i]
        print(f"{v.in_degree} {v.out_degree}")