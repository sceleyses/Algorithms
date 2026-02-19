def canDeliver(k, fields, prefix, R, B):
    for i in range(R - k + 1):
        mid = i + k // 2
        median = fields[mid]

        sumLeft = prefix[mid] - prefix[i]
        countLeft = mid - i
        left_sum = median * countLeft - sumLeft

        sumRight = prefix[i+k] - prefix[mid+1]
        countRight = i + k - mid - 1
        right_sum = sumRight - median * countRight

        cost = left_sum + right_sum
        if cost <= B:
            return True
    return False


def riceHub(fields, B, R):
    prefix = [0] * (R + 1)
    for i in range(R):
        prefix[i+1] = prefix[i] + fields[i]

    left = 1
    right = R
    while left <= right:
        m = (left + right) // 2
        if canDeliver(m, fields, prefix, R, B):
            left = m + 1
        else:
            right = m - 1
    return right


R, L, B = map(int, input().split())
fields = []
for _ in range(R):
    coordinate = int(input())
    fields.append(coordinate)
print(riceHub(fields, B, R))