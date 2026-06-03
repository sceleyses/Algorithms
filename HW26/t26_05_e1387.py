import math
from sys import maxsize as INF


class CableNetwork:
    def __init__(self, n, points):
        self.n = n
        self.points = points
        self.graph = self._to_graph()

    def _to_graph(self):
        matrix = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(i):
                x1, y1 = self.points[i]
                x2, y2 = self.points[j]

                dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                matrix[i][j] = dist
                matrix[j][i] = dist
        return matrix

    def get_min_cable_length(self):
        visited = [False for _ in range(self.n)]
        costs = [INF for _ in range(self.n)]
        costs[0] = 0.0

        total_cost = 0.0
        while True:
            i = -1
            cost_i = INF
            for j in range(self.n):
                if not visited[j] and costs[j] < cost_i:
                    i = j
                    cost_i = costs[j]

            if i == -1:
                break

            visited[i] = True
            total_cost += costs[i]

            for j in range(self.n):
                if i != j and not visited[j] and costs[j] > self.graph[i][j]:
                    costs[j] = self.graph[i][j]

        return total_cost


def main():
    f = open("input.txt")

    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        if not line:
            continue

        n = int(line)
        if n == 0:
            break

        points = []
        for _ in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))

        network = CableNetwork(n, points)
        min_length = network.get_min_cable_length()

        print(f"{min_length:.2f}")

    f.close()


if __name__ == '__main__':
    main()