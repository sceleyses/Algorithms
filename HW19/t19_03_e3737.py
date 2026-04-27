import sys


class Heap:
    def __init__(self):
        self._items = [0]

    def set_items(self, arr):
        self._items = [0] + arr

    def check_if_heap(self):
        n = len(self._items) - 1
        for pos in range(1, n // 2 + 1):
            left = 2 * pos
            right = 2 * pos + 1

            if left <= n and self._items[pos] > self._items[left]:
                return False

            if right <= n and self._items[right] is not None:
                if right <= n and self._items[pos] > self._items[right]:
                    return False
        return True


if __name__ == '__main__':
    input = sys.stdin.read().split()
    n = int(input[0])
    nums = list(map(int, input[1:]))

    h = Heap()
    h.set_items(nums)

    if h.check_if_heap():
        print("YES")
    else:
        print("NO")