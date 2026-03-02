
class Node:
    def __init__(self, phone: int):
        self.phone: int = phone
        self.next: Node | None = None


SIZE = 1000003
slots = [None] * SIZE
uniqueCount = 0


def hash(phone):
    return phone % SIZE


def add_phone(phone):
    global uniqueCount
    idx = hash(phone)

    node = slots[idx]
    while node is not None:
        if node.phone == phone:
            return
        node = node.next

    newNode = Node(phone)
    newNode.next = slots[idx]
    slots[idx] = newNode
    uniqueCount += 1



if __name__ == "__main__":
    n = int(input())
    numbers_found = 0
    while numbers_found < n:
        line = input().split()
        for number in line:
            add_phone(int(number))
            numbers_found += 1

    print(uniqueCount)
