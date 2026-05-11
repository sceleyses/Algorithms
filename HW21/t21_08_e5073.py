class Vertex:
    def __init__(self, key):
        self.key = key
        self.in_degree = []
        self.out_degree = []


class Graph:
    def __init__(self, n):
        self.mVertices = {i: Vertex(i) for i in range(1, n + 1)}

    def addEdgeAndCheck(self, u, v):
        if u in self.mVertices and v in self.mVertices:
            if v in self.mVertices[u].out_degree:
                return True
            self.mVertices[u].out_degree.append(v)
            self.mVertices[v].in_degree.append(v)
        return False


if __name__ == "__main__":
    f = open("input.txt", "r")

    line = f.readline().split()
    if line:
        n = int(line[0])
        m = int(line[1])

        g = Graph(n)
        marker = False

        for _ in range(m):
            edge_line = f.readline().split()
            if edge_line:
                u = int(edge_line[0])
                v = int(edge_line[1])
                if g.addEdgeAndCheck(u, v):
                    marker = True

    f.close()

    if marker:
        print("YES")
    else:
        print("NO")
