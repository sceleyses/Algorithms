class BinarySearchTree:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key is None:
            self.key = key
            return

        if key < self.key:
            if self.left is None:
                self.left = BinarySearchTree()
            self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BinarySearchTree()
            self.right.insert(key)

    def preorder(self):
        res = []
        if self.key is not None:
            res.append(self.key)
            if self.left:
                res.extend(self.left.preorder())
            if self.right:
                res.extend(self.right.preorder())
        return res


def main():
    batches = []
    while True:
        line = input().strip()
        if line == '*':
            break
        batches.append(line)

    bst = BinarySearchTree()

    for batch in reversed(batches):
        for char in batch:
            bst.insert(char)

    print("".join(bst.preorder()))


if __name__ == '__main__':
    main()