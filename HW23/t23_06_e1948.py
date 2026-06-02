WHITE = 0
GRAY = 1
BLACK = 2


class ColorVertex:
    def __init__(self, key):
        self.mKey = key
        self.mColor = WHITE
        self.mNeighbors = []

    def addNeighbor(self, neighbor_obj):
        self.mNeighbors.append(neighbor_obj)


class ColorGraph:
    def __init__(self, n):
        self.mVertices = {i: ColorVertex(i) for i in range(1, n + 1)}
        self.mStack = []
        self.mIsPossible = True

    def addEdge(self, u, v):
        if u in self.mVertices and v in self.mVertices:
            self.mVertices[u].addNeighbor(self.mVertices[v])

    def _iterative_dfs(self, start_vertex):
        dfs_stack = [[start_vertex, 0]]

        while dfs_stack:
            curr_data = dfs_stack[-1]
            u = curr_data[0]
            neighbor_idx = curr_data[1]

            if neighbor_idx == 0:
                u.mColor = GRAY

            found_next = False
            neighbors = u.mNeighbors

            for i in range(neighbor_idx, len(neighbors)):
                v = neighbors[i]
                if v.mColor == GRAY:
                    self.mIsPossible = False
                    return
                if v.mColor == WHITE:
                    curr_data[1] = i + 1
                    dfs_stack.append([v, 0])
                    found_next = True
                    break

            if not found_next:
                u.mColor = BLACK
                self.mStack.append(u.mKey)
                dfs_stack.pop()

    def get_topological_sort(self):
        self.mStack = []
        self.mIsPossible = True

        for i in range(1, len(self.mVertices) + 1):
            v = self.mVertices[i]
            if v.mColor == WHITE:
                self._iterative_dfs(v)
                if not self.mIsPossible:
                    return None

        return self.mStack[::-1]


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

    result = graph.get_topological_sort()

    if result is None:
        print("-1")
    else:
        print(*(result))