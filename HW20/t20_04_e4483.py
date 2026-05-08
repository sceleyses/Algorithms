class Tree:
    def __init__(self, data, n):
        self.n = n
        self.min_tree = [0] * (2 * n)
        self.max_tree = [0] * (2 * n)

        for i in range(n):
            idx = n + i
            val = data[i]
            self.min_tree[idx] = val
            self.max_tree[idx] = val

        for i in range(n - 1, 0, -1):
            self.min_tree[i] = min(self.min_tree[2 * i], self.min_tree[2 * i + 1])
            self.max_tree[i] = max(self.max_tree[2 * i], self.max_tree[2 * i + 1])

    def update(self, i, val):
        idx = i + self.n
        self.min_tree[idx] = val
        self.max_tree[idx] = val
        while idx > 1:
            idx //= 2
            left, right = 2 * idx, 2 * idx + 1
            new_min = min(self.min_tree[left], self.min_tree[right])
            new_max = max(self.max_tree[left], self.max_tree[right])

            if self.min_tree[idx] == new_min and self.max_tree[idx] == new_max:
                break

            self.min_tree[idx] = new_min
            self.max_tree[idx] = new_max

    def query_is_equal(self, l, r):
        res_min = 10 ** 9
        res_max = -1
        l += self.n
        r += self.n

        while l <= r:
            if l % 2 == 1:
                if self.min_tree[l] < res_min: res_min = self.min_tree[l]
                if self.max_tree[l] > res_max: res_max = self.max_tree[l]
                l += 1
            if r % 2 == 0:
                if self.min_tree[r] < res_min: res_min = self.min_tree[r]
                if self.max_tree[r] > res_max: res_max = self.max_tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res_min == res_max


if __name__ == "__main__":
    line1 = input().split()
    n = int(line1[0])

    a = list(map(int, input().split()))

    st = Tree(a, n)

    line3 = input().split()
    m = int(line3[0])

    for _ in range(m):
        q_type, l, r = map(int, input().split())
        if q_type == 1:
            if st.query_is_equal(l - 1, r - 1):
                print("draw")
            else:
                print("wins")
        else:
            st.update(l - 1, r)