import sys
from collections import deque


class LinesSolver:
    def __init__(self):
        self.size = 0
        self.matrix = []
        self.start = None
        self.target = None

    def read_input(self):
        input_data = sys.stdin.read().split()
        if not input_data:
            return False

        self.size = int(input_data[0])
        raw_rows = input_data[1:self.size + 1]

        for r_idx, row_str in enumerate(raw_rows):
            row = list(row_str)
            self.matrix.append(row)
            for c_idx, char in enumerate(row):
                if char == '@':
                    self.start = (r_idx, c_idx)
                elif char == 'X':
                    self.target = (r_idx, c_idx)
        return True

    def solve(self):
        if not self.start or not self.target:
            sys.stdout.write("N\n")
            return

        path = self._find_bfs_path()

        if path:
            sys.stdout.write("Y\n")
            self._mark_path(path)
            result = "\n".join("".join(row) for row in self.matrix) + "\n"
            sys.stdout.write(result)
        else:
            sys.stdout.write("N\n")

    def _find_bfs_path(self):
        queue = deque([self.start])
        parent_cells = {self.start: None}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            curr_row, curr_col = queue.popleft()

            if (curr_row, current_col := curr_col) == self.target:
                return self._reconstruct_path(parent_cells)

            for dr, dc in directions:
                nr, nc = curr_row + dr, curr_col + dc
                neighbor = (nr, nc)

                if 0 <= nr < self.size and 0 <= nc < self.size:
                    if neighbor not in parent_cells and self.matrix[nr][nc] in ('.', 'X'):
                        parent_cells[neighbor] = (curr_row, curr_col)
                        queue.append(neighbor)

        return None

    def _reconstruct_path(self, parent_cells):
        path = []
        curr = self.target
        while curr is not None:
            path.append(curr)
            curr = parent_cells[curr]
        return path[::-1]

    def _mark_path(self, path):
        for r, c in path[1:]:
            self.matrix[r][c] = '+'


def main():
    solver = LinesSolver()
    if solver.read_input():
        solver.solve()


if __name__ == "__main__":
    main()