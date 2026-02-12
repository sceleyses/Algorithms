def cycleShifts(x):
    left = int(x, 2)
    k = len(x)
    right = 2**k - 1
    xx = x+x
    while left < right:
        m = left + (right - left) // 2
        if bin(m)[2:] in xx:
            left = m+1
        else:
            right = m
    return right-1

n = int(input())
x = bin(n)[2:]
print(cycleShifts(x))