import sys

INF = sys.maxsize


class Node:
    def __init__(self, key):
        self.key = key
        self.neighbors = []
        self.weights = []


class Graph:
    def __init__(self, n):
        self.elements = [Node(i) for i in range(n)]
        self.length = n

    def add_edge(self, start, end, weight):
        self.elements[start].neighbors.append(self.elements[end])
        self.elements[start].weights.append(weight)

    def ford_bellman(self, start, end):
        n = self.length
        distances = [INF for _ in range(n)]
        distances[start] = 0

        for _ in range(n - 1):
            relaxed = True
            for i in range(n):

                for j in range(len(self.elements[i].neighbors)):
                    neighbor_node = self.elements[i].neighbors[j]
                    weight = self.elements[i].weights[j]

                    v = neighbor_node.key

                    if distances[i] != INF and distances[v] > distances[i] + weight:
                        distances[v] = distances[i] + weight
                        relaxed = False
            if relaxed:
                break

        if distances[end] < INF:
            return distances[end]
        else:
            return 30000


if __name__ == "__main__":
    f = open("input.txt")
    line1 = f.readline().split()
    if not line1:
        sys.exit()

    n, m = map(int, line1)
    graph = Graph(n)
    for _ in range(m):
        line = f.readline().split()
        if line:
            i, j, w = map(int, line)
            graph.add_edge(i - 1, j - 1, w)
    f.close()

    ans = []

    for i in range(n):
        ans.append(graph.ford_bellman(0, i))

    print(*ans)