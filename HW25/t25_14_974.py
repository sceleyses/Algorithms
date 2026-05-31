class Graph:
    def __init__(self, matrix, n):
        self.matrix = matrix
        self.n = n

    def floyd(self):
        dist = [row[:] for row in self.matrix]

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

if __name__ == "__main__":
    f = open("input.txt")
    line = f.readline()
    n = int(line.strip())
    matrix = []
    for _ in range(n):
        row = list(map(int, f.readline().split()))
        matrix.append(row)
    f.close()
    g = Graph(matrix, n)
    result = g.floyd()
    for row in result:
        print(*(row))