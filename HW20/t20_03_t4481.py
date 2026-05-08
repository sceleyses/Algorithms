class TreeGCD:
    def __init__(self, data, n):
        self.n = n
        self.tree = [0] * (2 * n)

        for i in range(n):
            self.tree[n + i] = data[i]

        for i in range(n - 1, 0, -1):
            self.tree[i] = self.get_gcd(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, val):
        idx = i + self.n
        self.tree[idx] = val
        while idx > 1:
            idx //= 2
            new_gcd = self.get_gcd(self.tree[2 * idx], self.tree[2 * idx + 1])
            if self.tree[idx] == new_gcd:
                break
            self.tree[idx] = new_gcd

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n

        while l <= r:
            if l % 2 == 1:
                if res == 0:
                    res = self.tree[l]
                else:
                    res = self.get_gcd(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                if res == 0:
                    res = self.tree[r]
                else:
                    res = self.get_gcd(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

    def get_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


if __name__ == "__main__":
    n_input = input().split()
    n = int(n_input[0])

    a = list(map(int, input().split()))

    m_input = input().split()
    m = int(m_input[0])

    st = TreeGCD(a, n)

    for _ in range(m):
        q_type, l, r = map(int, input().split())

        if q_type == 1:
            print(st.query(l - 1, r - 1))
        else:
            st.update(l - 1, r)