class Vertex:
    def __init__(self, key):
        self.mKey = key
        self.in_degree = []
        self.out_degree = []

class Graph:
    def __init__(self, n):
        self.mVertices = {i: Vertex(i) for i in range(1, n + 1)}
        self.visited = [False] * (n + 1)
        self.count = 0

    def addEdge(self, u, v):
        if u in self.mVertices and v in self.mVertices:
            self.mVertices[u].out_degree.append(v)
            self.mVertices[v].in_degree.append(u)

    def find_paths(self, current, target, d, current_d):
        if current_d > d:
            return
        if current == target:
            self.count += 1
            return

        self.visited[current] = True
        for neighbor in self.mVertices[current].out_degree:
            if not self.visited[neighbor]:
                self.find_paths(neighbor, target, d, current_d + 1)
        self.visited[current] = False

if __name__ == "__main__":
    with open("input.txt") as f:
        data = map(int, f.read().split())
        it = iter(data)
        n = next(it)
        k = next(it)
        a = next(it)
        b = next(it)
        d = next(it)

        g = Graph(n)
        for _ in range(k):
            u, v = next(it), next(it)
            g.addEdge(u, v)

        g.find_paths(a, b, d, 0)
        print(g.count)