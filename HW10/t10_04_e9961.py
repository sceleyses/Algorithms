def solve():
    try:
        line = input().split()
        if not line: return
        n, k = map(int, line)
    except EOFError:
        return

    def backtrack(current_permutation, used):
        if len(current_permutation) == k:
            print(*(current_permutation))
            return

        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                current_permutation.append(i)

                backtrack(current_permutation, used)

                current_permutation.pop()
                used[i] = False

    used = [False] * (n + 1)
    backtrack([], used)


if __name__ == "__main__":
    solve()