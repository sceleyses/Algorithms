class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self.topNode = None

    def push(self, number):
        newNode = Node(number)
        newNode.next = self.topNode

        self.topNode = newNode

    def empty(self):
        return self.topNode is None

    def pop(self):
        if self.empty():
            raise Exception("Stack: 'pop' applied to empty container")

        top = self.topNode
        item = top.item
        self.topNode = self.topNode.next
        del top
        return item


def convert(number, base):
    if number == 0:
        return "0"

    stack = Stack()
    while number > 0:
        stack.push(number % base)
        number //= base

    result = []
    while not stack.empty():
        digit = stack.pop()
        if digit < 10:
            result.append(str(digit))
        else:
            result.append(f"[{digit}]")

    return "".join(result)

a = int(input())
p = int(input())
print(convert(a, p))