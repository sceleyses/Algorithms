
class Node:
    def __init__(self, key):
        self.key = key
        self.used = False
        self.next = None


SIZE = 2003
slots = [None] * SIZE


def hash(key: str) -> int:
    ans = 0
    p = 29
    for k in key:
        ans = ans * p + ord(k)
    return ans % SIZE


def addToVocabulary(word: str):
    word = word.lower()
    idx = hash(word)
    node = slots[idx]
    while node:
        if node.key == word:
            return
        node = node.next

    newNode = Node(word)
    newNode.next = slots[idx]
    slots[idx] = newNode


def markAsUsed(word: str) -> bool:
    word = word.lower()
    idx = hash(word)
    node = slots[idx]
    while node:
        if node.key == word:
            node.used = True
            return True
        node = node.next
    return False


def main():
    line = input().split()
    n = int(line[0])
    m = int(line[1])

    for _ in range(n):
        word = input().strip()
        if word:
            addToVocabulary(word)

    fullTextLines = []
    for _ in range(m):
        fullTextLines.append(input())

    fullText = " ".join(fullTextLines)

    punctuation = ".,:;-−'\"!?"
    for char in punctuation:
        fullText = fullText.replace(char, ' ')

    wordsInText = fullText.split()
    for w in wordsInText:
        if not markAsUsed(w):
            print("Some words from the text are unknown.")
            return

    for i in range(SIZE):
        node = slots[i]
        while node:
            if not node.used:
                print("The usage of the vocabulary is not perfect.")
                return
            node = node.next

    print("Everything is going to be OK.")


if __name__ == "__main__":
    main()