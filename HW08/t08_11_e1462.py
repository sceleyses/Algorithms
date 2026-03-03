def sort(arr, n):
    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            last_digit_j = arr[j] % 10
            last_digit_min = arr[min_idx] % 10

            if last_digit_j < last_digit_min:
                min_idx = j
            elif last_digit_j == last_digit_min:
                if arr[j] < arr[min_idx]:
                    min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


n = int(input())
arr = []
while len(arr) < n:
    line = input().split()
    for x in line:
        arr.append(int(x))

sort(arr, n)

print(*(arr))