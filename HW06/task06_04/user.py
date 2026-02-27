
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class Node:

    def __init__(self, key: str, value: str):
        self.key: str = key
        self.value: list[str] = value
        self.next: Node | None = None


size: int = 1000003
slots: list[Node | None]


def hash(key: str) -> int:
    ans = 0
    p = 29
    for k in key:
        ans = ans * p + ord(k)
    return ans % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots
    slots = [None for _ in range(size)]

def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    i = hash(author)
    node = slots[i]
    while node is not None:
        if node.key == author:
            if title not in node.value:
                node.value.append(title)
            return
        node = node.next

    new_node = Node(author, [title])
    new_node.next = slots[i]
    slots[i] = new_node


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    i = hash(author)
    node = slots[i]
    while node is not None:
        if node.key == author:
            return title in node.value
        node = node.next
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    i = hash(author)
    node = slots[i]
    prev = None
    while node is not None:
        if node.key == author:
            if title in node.value:
                node.value.remove(title)
                if not node.value:
                    if prev is None:
                        slots[i] = node.next
                    else:
                        prev.next = node.next
            return
        prev = node
        node = node.next


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    i = hash(author)
    node = slots[i]
    while node is not None:
        if node.key == author:
            return node.value
        node = node.next
    return []

