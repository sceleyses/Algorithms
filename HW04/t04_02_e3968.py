import math
def f(x):
    return x**2 + math.sqrt(x)

def squareRoot(C):
    left = 0
    right = C
    m = (left + right) / 2.0
    while left != m and m != right:
        if f(m) < C:
            left = m
        else:
            right = m
        m = (left + right) / 2.0
    return left

C = float(input().strip())
result = squareRoot(C)
print(f'{result:.9f}')