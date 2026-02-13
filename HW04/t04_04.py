import math

def f(x):
    return math.sin(x) - x/3

def binary():
    left = 1.6
    right = 3.0
    m = (right + left) / 2.0
    while left != m and m != right:
        if f(m) <= 0:
            left = m
        else:
            right = m
        m = (right + left) / 2.0
    return left

x = binary()
with open("t04_04_result.txt", "w") as file:
    file.write(f"{x}")
    file.close()