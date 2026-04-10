class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def push_front(self, item):
        new_node = Node(item)
        if self._count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._count += 1
        print("ok")

    def push_back(self, item):
        new_node = Node(item)
        if self._count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._count += 1
        print("ok")

    def pop_front(self):
        if self._count == 0:
            print("error")
            return
        elif self._count == 1:
            print(self.head.item)
            self.head = None
            self.tail = None
        else:
            print(self.head.item)
            self.head = self.head.next
            self.head.prev = None
        self._count -= 1


    def pop_back(self):
        if self._count == 0:
            print("error")
            return
        elif self._count == 1:
            print(self.tail.item)
            self.head = None
            self.tail = None
        else:
            print(self.tail.item)
            self.tail = self.tail.prev
            self.tail.next = None
        self._count -= 1


    def front(self):
        if self._count == 0:
            print("error")
            return
        else:
            print(self.head.item)

    def back(self):
        if self._count == 0:
            print("error")
            return
        else:
            print(self.tail.item)

    def size(self):
        print(self._count)

    def clear(self):
        self.head = None
        self.tail = None
        self._count = 0
        print("ok")

    def exit(self):
        print("bye")


q = Queue()
while True:
    try:
        line = input().split()
        if not line: continue

        command = line[0]
        if command == "push_front":
            q.push_front(line[1])
        elif command == "push_back":
            q.push_back(line[1])
        elif command == "pop_front":
            q.pop_front()
        elif command == "pop_back":
            q.pop_back()
        elif command == "front":
            q.front()
        elif command == "back":
            q.back()
        elif command == "size":
            q.size()
        elif command == "clear":
            q.clear()
        elif command == "exit":
            q.exit()
            break
    except EOFError:
        break