class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def empty(self):
        return self._top is None

    def push(self, item):
        node = Node(item)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        if self.empty():
            return None
        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item

    def back(self):
        if self.empty():
            return None
        return self._top.item


if __name__ == "__main__":
    while True:
        line = input().split()
        if not line: continue

        n = int(line[0])
        if n == 0: break

        while True:
            line = input().split()
            if not line: continue

            if int(line[0]) == 0:
                print()
                break

            target = [int(x) for x in line]
            while len(target) < n:
                target.extend([int(x) for x in input().split()])

            stack = Stack()
            current_wagon = 1
            possible = True

            for wagon_to_find in target:
                if not stack.empty() and stack.back() == wagon_to_find:
                    stack.pop()
                else:
                    while current_wagon <= n and (stack.empty() or stack.back() != wagon_to_find):
                        stack.push(current_wagon)
                        current_wagon += 1

                    if stack.back() == wagon_to_find:
                        stack.pop()
                    else:
                        possible = False
                        break

            if possible:
                print("Yes")
            else:
                print("No")
