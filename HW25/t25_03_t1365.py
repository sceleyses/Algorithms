import sys
import heapq

INF = sys.maxsize


class Graph():
    def __init__(self, matrix):
        self.matrix = matrix

    def dijkstra(self, start, end):
        n = len(self.matrix)
        distances = [INF for _ in range(n)]
        distances[start] = 0

        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            current_dist, element = heapq.heappop(pq)

            if current_dist > distances[element]:
                continue

            for i in range(n):
                if self.matrix[element][i] != -1 and element != i:
                    if distances[i] > distances[element] + self.matrix[element][i]:
                        distances[i] = distances[element] + self.matrix[element][i]
                        heapq.heappush(pq, (distances[i], i))

        if distances[end] == INF:
            print(-1)
        else:
            print(distances[end])


if __name__ == "__main__":
    with open("input.txt") as file:
        n, s, f = file.readline().split()
        n, s, f = int(n), int(s), int(f)
        matrix = []

        for i in range(n):
            line = list(map(int, file.readline().split()))
            matrix.append(line)

    g = Graph(matrix)
    g.dijkstra(s - 1, f - 1)