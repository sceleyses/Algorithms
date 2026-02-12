def ardentButterflyCollector(collection, m):
    left = 0
    right = len(collection)
    while left < right:
        middle = left + (right - left) // 2
        if collection[middle] < m:
            left = middle + 1
        else:
            right = middle  
    return collection[right] == m


n = int(input())
collection = list(map(int, input().split()))
m = int(input())
checking = list(map(int, input().split()))

for k in range(0, m):
    if ardentButterflyCollector(collection, checking[k]):
        print("YES")
    else:
        print("NO")