def merge_sort(array):
    if len(array) <= 1:
        return

    m = len(array) // 2
    left = array[:m]
    right = array[m:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    n = int(input())

    robots = []
    for _ in range(n):
        data = input().split()
        if data:
            first = int(data[0])
            second = int(data[1])
            robots.append([first, second])

    merge_sort(robots)

    for r in robots:
        print(r[0], r[1])