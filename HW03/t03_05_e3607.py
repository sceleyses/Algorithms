def sortByGrowth(left, right, n):
    count = 0
    for i in range(len(n)):
        if n[i] <= right and n[i] >= left:
            count += 1
    return count

while True:
    numbers = int(input())
    n = list(map(int, input().split()))
    left, right = map(int, input().split())
    print(sortByGrowth(left, right, n))
