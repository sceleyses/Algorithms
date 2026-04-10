class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def push(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1
        print("ok")

    def pop(self):
        if self._count == 0:
            print("error")
        else:
            print(self.head.item)
            self.head = self.head.next
            self._count -= 1
            if self.head is None:
                self.tail = None

    def front(self):
        if self._count == 0:
            print("error")
        else:
            print(self.head.item)

    def size(self):
        return self._count

    def clear(self):
        self.head = None
        self.tail = None
        self._count = 0
        print("ok")



q = Queue()
while True:
    try:
        line = input().split()
        if not line: continue

        command = line[0]
        if command == "push":
            q.push(line[1])
        elif command == "pop":
            q.pop()
        elif command == "front":
            q.front()
        elif command == "size":
            print(q.size())
        elif command == "clear":
            q.clear()
        elif command == "exit":
            print("bye")
            break
    except EOFError:
        break