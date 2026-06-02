class Vertex:
    def __init__(self, key):
        self.mKey = key
        self.mNeighbors = []
        self.mVisited = False

    def addNeighbor(self, neighbor_obj):
        self.mNeighbors.append(neighbor_obj)


class Graph:
    def __init__(self, n):
        self.mVertices = {i: Vertex(i) for i in range(1, n + 1)}

    def addEdge(self, u, v):
        if u in self.mVertices and v in self.mVertices:
            self.mVertices[u].addNeighbor(self.mVertices[v])
            self.mVertices[v].addNeighbor(self.mVertices[u])

    def find_components(self):
        components = []

        for i in range(1, len(self.mVertices) + 1):
            v = self.mVertices[i]
            if not v.mVisited:
                component = []
                stack = [v]
                v.mVisited = True

                while stack:
                    curr = stack.pop()
                    component.append(curr.mKey)

                    for neighbor in curr.mNeighbors:
                        if not neighbor.mVisited:
                            neighbor.mVisited = True
                            stack.append(neighbor)

                components.append(component)

        return components


if __name__ == "__main__":
    f = open("input.txt")
    data = f.read().split()
    f.close()

    if data:
        n, m = int(data[0]), int(data[1])
        graph = Graph(n)

        idx = 2
        for _ in range(m):
            if idx + 1 < len(data):
                graph.addEdge(int(data[idx]), int(data[idx + 1]))
                idx += 2

        components = graph.find_components()

        print(len(components))
        for comp in components:
            print(len(comp))
            print(*(comp))