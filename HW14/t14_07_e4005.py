class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            return False
        else:
            ans_item = self.head.item
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return ans_item

def main(q1, q2, n):
    counter = 0
    while True:
        top1 = q1.pop()
        top2 = q2.pop()
        if top1 == 0 and top2 == n-1:
            q1.push(top1)
            q1.push(top2)
        elif top2 == 0 and top1 == n-1:
            q2.push(top1)
            q2.push(top2)
        elif top1 > top2:
            q1.push(top1)
            q1.push(top2)
        else:
            q2.push(top1)
            q2.push(top2)

        counter += 1
        if counter == 2*10**5:
            print("draw")
            return
        elif q1.is_empty():
            print(f"second {counter}")
            return
        elif q2.is_empty():
            print(f"first {counter}")
            return

if __name__== ("__main__"):
    n = int(input())
    first_items = []
    secod_items = []
    while len(first_items) < n/2:
        line = input().split()
        first_items.extend(map(int, line))
    while len(secod_items) < n/2:
        line = input().split()
        secod_items.extend(map(int, line))

    q1 = Queue()
    q2 = Queue()
    for i in range(0,int(n/2)):
        q1.push(first_items[i])
        q2.push(secod_items[i])

    main(q1, q2, n)

