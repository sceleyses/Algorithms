class Tree:
    def __init__(self, tree_id):
        self.tree_id = tree_id
        self.children = []
        self.value = None

    def add_child(self, child_node):
        self.children.append(child_node)

    def evaluate(self, depth):
        if not self.children:
            return self.value

        child_values = [child.evaluate(depth + 1) for child in self.children]

        if depth % 2 == 0:
            return max(child_values)
        else:
            return min(child_values)


if __name__ == "__main__":
    line = input().strip()
    if not line:
        exit()
    n = int(line)

    trees = [Tree(i) for i in range(n + 1)]

    for i in range(2, n + 1):
        parts = input().split()
        if not parts:
            continue

        tree_type = parts[0]
        parent_id = int(parts[1])

        trees[parent_id].add_child(trees[i])

        if tree_type == 'L':
            trees[i].value = int(parts[2])

    root = trees[1]
    result = root.evaluate(0)

    if result == 1:
        print("+1")
    else:
        print(result)