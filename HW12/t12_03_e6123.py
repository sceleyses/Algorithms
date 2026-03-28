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
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item

    def back(self):
        if self.empty():
            return "error"
        return self._top.item

    def size(self):
        return self._size

    def clear(self):
        self._top = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command_line: str):
        # Розбиваємо рядок на частини і прибираємо зайві пробіли
        parts = command_line.split()
        if not parts:
            return None

        command = parts[0]

        if command == "push":
            return self.push(parts[1])
        elif command == "pop":
            return self.pop()
        elif command == "back":
            return self.back()
        elif command == "size":
            return self.size()
        elif command == "clear":
            return self.clear()
        elif command == "exit":
            return self.exit()
        return "error"


if __name__ == "__main__":
    stack = Stack()

    while True:
        line = input().strip()
        if not line:
            continue
        res = stack.execute(line)
        if res is not None:
            print(res)
            if res == "bye":
                break