def f(x):
    return x**3 + 4*x**2 + x

def binary():
    left = 0
    right = 2
    m = (right + left) / 2.0
    while left != m and m != right:
        if f(m) < 6:
            left = m
        else:
            right = m
        m = (right + left) / 2.0
    return left

x = binary()
with open("t04_05_result.txt", "w") as file:
    file.write(f"{x}")
    file.close