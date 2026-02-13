def f(x):
    return x**3 + x

def binary():
    left = 0
    right = 10
    m = (left + right) / 2.0
    while left != m and m != right:
        if f(m) > 4:
            right = m
        else:
            left = m
        m = (left + right) / 2.0
    return left

x = binary()
with open("t04_03_result.txt", "w") as file:
    file.write(f"{x}")
    file.close()
