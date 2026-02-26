"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

keys: list[str]
values: list[list[str]]
EMPTY = "EMPTY"
DELETED = "DELETED"
size: int = 1000000
count: int


def hash(key: str) -> int:
    ans = 0
    p = 29
    for k in key:
        ans = ans * p + ord(k)
    return ans % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global keys, values, count
    count = 0
    keys = [EMPTY for _ in range(size)]
    values = [EMPTY for _ in range(size)]


def addBook(author, title) -> None:
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global count
    i = hash(author)
    j = -1
    while keys[i] is not EMPTY:
        if keys[i] == author:
            if title not in values[i]:
                values[i].append(title)
            return
        if j == -1 and keys[i] == DELETED:
            j = i
        i = (i + 1) % size

    if j == -1:
        j = i

    keys[j] = author
    values[j] = [title]
    count += 1


def find(author, title):
    """ Перевіряє чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    i = hash(author)
    while keys[i] is not EMPTY:
        if keys[i] == author:
            return title in values[i]
        i = (i + 1) % size
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global count
    i = hash(author)
    while keys[i] is not EMPTY:
        if keys[i] == author:
            if title in values[i]:
                values[i].remove(title)
                if not values[i]:
                    keys[i] = DELETED
                    values[i] = DELETED
                    count -= 1
            return
        i = (i + 1) % size


def findByAuthor(author):
    """ Повертає список книг заданого автора у алфавітному порядку.
    Якщо бібліотека не містить книг заданого автора, повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    i = hash(author)
    while keys[i] is not EMPTY:
        if keys[i] == author:
            return values[i]
        i = (i + 1) % size
    return []
