class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None


class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв'язного Списку"""
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        """Вивести елементи Зв'язного Списку"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

    def PrintReverse(self) -> None:
        """Вивести елементи Зв'язного Списку в зворотному порядку"""
        res = []
        self._print_recursive(self.head, res)
        print(" ".join(res))

    def _print_recursive(self, node: Node, res: list) -> None:
        if node is None:
            return
        self._print_recursive(node.next, res)
        res.append(str(node.data))


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    linked_list = List()
    for num in numbers:
        linked_list.addToTail(num)

    linked_list.Print()
    linked_list.PrintReverse()