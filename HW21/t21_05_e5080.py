class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    def hanging_vertex(self, vertex):
        return sum(self.matrix[vertex]) == 1


if __name__ == "__main__":
    f = open("input.txt", "r")

    line_n = f.readline().strip()
    if line_n:
        n = int(line_n)
        matrix = []

        for i in range(n):
            line = list(map(int, f.readline().split()))
            matrix.append(line)

        f.close()

        g = Graph(matrix)
        answer = 0
        for i in range(n):
            if g.hanging_vertex(i):
                answer += 1
        print(answer)            