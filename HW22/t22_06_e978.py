from collections import deque


class Vertex:
    def __init__(self, key):
        self.mKey = key
        self.out_degree = []
        self.burn_time = -1


class Graph:
    def __init__(self, n):
        self.mVertices = {i: Vertex(i) for i in range(1, n + 1)}

    def addEdge(self, u, v):
        if u in self.mVertices and v in self.mVertices:
            self.mVertices[u].out_degree.append(v)
            self.mVertices[v].out_degree.append(u)

    def start_fire(self, start_nodes):
        queue = deque()

        for node_idx in start_nodes:
            vertex = self.mVertices[node_idx]
            vertex.burn_time = 0
            queue.append(node_idx)

        max_time = 0
        last_vertex_key = 0

        while queue:
            u_key = queue.popleft()
            u_vertex = self.mVertices[u_key]

            if u_vertex.burn_time > max_time:
                max_time = u_vertex.burn_time
                last_vertex_key = u_key
            elif u_vertex.burn_time == max_time:
                if last_vertex_key == 0 or u_key < last_vertex_key:
                    last_vertex_key = u_key
            elif last_vertex_key == 0:
                last_vertex_key = u_key

            for v_key in u_vertex.out_degree:
                v_vertex = self.mVertices[v_key]
                if v_vertex.burn_time == -1:
                    v_vertex.burn_time = u_vertex.burn_time + 1
                    queue.append(v_key)

        return max_time, last_vertex_key


if __name__ == "__main__":
    line1 = input().split()
    if line1:
        n, m = map(int, line1)

        g = Graph(n)
        for _ in range(m):
            u, v = map(int, input().split())
            g.addEdge(u, v)

        k = int(input())
        start_nodes = list(map(int, input().split()))

        time, node = g.start_fire(start_nodes)

        print(time)
        print(node)