class Graph:
    def __init__(self, n):
        self.vertices_count = n
        self.unique_edges = set()

    def addEdge(self, u, v):
        if u != v and 1 <= u <= self.vertices_count and 1 <= v <= self.vertices_count:
            edge = (min(u, v), max(u, v))
            self.unique_edges.add(edge)

    def check(self):
        expected_count = (self.vertices_count * (self.vertices_count - 1)) // 2
        return len(self.unique_edges) == expected_count


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

    if g.check():
        print("YES")
    else:
        print("NO")