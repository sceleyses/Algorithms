class TreeNode:
    def __init__(self, node_id, color):
        self.node_id = node_id
        self.color = color
        self.children = []
        self.result = 0
        self.color_set = set()


def solve(line, n):
    nodes = [None] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    root_id = -1

    for i in range(1, n + 1):
        p, c = map(int, input().split())
        nodes[i] = TreeNode(i, c)
        if p == 0:
            root_id = i
        else:
            adj[p].append(i)

    stack = [(root_id, False)]
    visit_order = []

    while stack:
        u, visited = stack.pop()
        if visited:
            visit_order.append(u)
        else:
            stack.append((u, True))
            for v in adj[u]:
                stack.append((v, False))

    for u_id in visit_order:
        curr_node = nodes[u_id]
        curr_node.color_set = {curr_node.color}

        largest_child_set = None
        best_v = -1

        for v_id in adj[u_id]:
            child_set = nodes[v_id].color_set
            if largest_child_set is None or len(child_set) > len(largest_child_set):
                largest_child_set = child_set
                best_v = v_id

        if largest_child_set is not None:
            target_set = nodes[best_v].color_set
            target_set.add(curr_node.color)

            for v_id in adj[u_id]:
                if v_id != best_v:
                    target_set.update(nodes[v_id].color_set)
                    nodes[v_id].color_set = None

            curr_node.color_set = target_set

        curr_node.result = len(curr_node.color_set)

    print(*(nodes[i].result for i in range(1, n + 1)))


if __name__ == "__main__":
    line = input().split()
    n = int(line[0])
    solve(line, n)