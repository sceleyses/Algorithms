def mutantsFirstOccurrence(animalsColours, colour):
    left = 0
    right = len(animalsColours)
    while left < right:
        m = left + (right - left) // 2
        if animalsColours[m] < colour:
            left = m + 1
        else:
            right = m
    if left < len(animalsColours) and animalsColours[left] == colour:
        return left
    return -1

def mutantsLastOccurrence(animalsColours, colour):
    left = 0
    right = len(animalsColours)
    while left < right:
        m = left + (right - left) // 2
        if animalsColours[m] <= colour:
            left = m + 1
        else:
            right = m
    if left > 0 and animalsColours[left-1] == colour:
        return left - 1
    return -1

n = int(input())
animalsColours = list(map(int, input().split()))
m = int(input())
colours = list(map(int, input().split()))

for colour in colours:
    first = mutantsFirstOccurrence(animalsColours, colour)
    if first == -1:
        print(0)
    else:
        last = mutantsLastOccurrence(animalsColours, colour)
        print(last-first+1)