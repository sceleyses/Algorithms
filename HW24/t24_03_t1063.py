import sys
from collections import deque


class IslandCounter:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.matrix = []
        self.visited = set()

    def read_input(self):
        input_data = sys.stdin.read().split()
        if not input_data:
            return False

        self.rows = int(input_data[0])
        self.cols = int(input_data[1])
        self.matrix = input_data[2:self.rows + 2]
        return True

    def solve(self):
        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.matrix[r][c] == '#' and (r, c) not in self.visited:
                    self._bfs(r, c)
                    count += 1

        sys.stdout.write(str(count) + "\n")

    def _bfs(self, start_r, start_c):
        queue = deque([(start_r, start_c)])
        self.visited.add((start_r, start_c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc

                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.matrix[nr][nc] == '#' and (nr, nc) not in self.visited:
                        self.visited.add((nr, nc))
                        queue.append((nr, nc))


def main():
    solver = IslandCounter()
    if solver.read_input():
        solver.solve()


if __name__ == "__main__":
    main()