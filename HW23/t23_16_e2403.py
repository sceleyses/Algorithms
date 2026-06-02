WHITE = 0
GRAY = 1
BLACK = 2


class ColorVertex:
    def __init__(self, key):
        self.mKey = key
        self.mColor = WHITE
        self.mNeighbors = []
        self.mRevNeighbors = []

    def addNeighbor(self, neighbor):
        self.mNeighbors.append(neighbor)
        neighbor.mRevNeighbors.append(self)


class ColorGraph:
    def __init__(self, n):
        self.mVertices = {i: ColorVertex(i) for i in range(1, n + 1)}

    def addEdge(self, u, v):
        if u in self.mVertices and v in self.mVertices:
            self.mVertices[u].addNeighbor(self.mVertices[v])

    def _dfs_forward(self, v, stack):
        v.mColor = GRAY
        for neighbor in v.mNeighbors:
            if neighbor.mColor == WHITE:
                self._dfs_forward(neighbor, stack)
        v.mColor = BLACK
        stack.append(v)

    def _dfs_backward(self, v):
        v.mColor = GRAY
        for neighbor in v.mRevNeighbors:
            if neighbor.mColor == WHITE:
                self._dfs_backward(neighbor)
        v.mColor = BLACK

    def get_scc_count(self):
        stack = []

        for i in range(1, len(self.mVertices) + 1):
            v = self.mVertices[i]
            if v.mColor == WHITE:
                self._dfs_forward(v, stack)

        for v in self.mVertices.values():
            v.mColor = WHITE

        scc_count = 0
        while stack:
            v = stack.pop()
            if v.mColor == WHITE:
                scc_count += 1
                self._dfs_backward(v)

        return scc_count


if __name__ == "__main__":
    f = open("input.txt", "r")
    data = f.read().split()
    f.close()

    n, m = int(data[0]), int(data[1])
    graph = ColorGraph(n)

    idx = 2
    for _ in range(m):
        if idx + 1 < len(data):
            graph.addEdge(int(data[idx]), int(data[idx + 1]))
            idx += 2

    print(graph.get_scc_count())