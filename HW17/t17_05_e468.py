import sys
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTPathChecker:
    def __init__(self):
        self.root = None

    def check_path(self, arr):

        self.root = Node(arr[0])

        low = -2147483648
        high = 2147483647

        current = self.root

        for x in arr[1:]:
            if not (low <= x <= high):
                return False

            if x < current.key:
                if current.left is not None:
                    return False 
                current.left = Node(x)
                high = current.key
                current = current.left

            else:
                if current.right is not None:
                    return False
                current.right = Node(x)
                low = current.key
                current = current.right

        return True

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    checker = BSTPathChecker()
    print("YES" if checker.check_path(data) else "NO")