import sys


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self._counter = 0

    def AddToTail(self, val: int) -> None:
        """Додати число val у кінець зв'язаного списку"""
        new_node = Node(val)
        if self._counter == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._counter += 1

    def RotateRight(self, k: int) -> None:
        k = k % self._counter
        if k == 0 or self._counter == 0:
            return

        self.tail.next = self.head
        for _ in range((self._counter - k)):
            self.tail = self.tail.next

        self.head = self.tail.next
        self.tail.next = None

    def Print(self) -> None:
        """Вивести елементи зв'язаного списку"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))


if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if not input_data:
        exit()

    n = int(input_data[0])
    numbers = list(map(int, input_data[1:n + 1]))
    ks = list(map(int, input_data[n + 1:]))

    my_list = List()
    for num in numbers:
        my_list.AddToTail(num)

    for k in ks:
        my_list.RotateRight(k)
        my_list.Print()