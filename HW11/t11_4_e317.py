import sys
def karatsuba(a, b):
    if a < 10 or b < 10:
        return a * b

    n = max(len(str(a)), len(str(b)))
    m = n // 2

    high1 = a // 10**m
    low1 = a % 10**m
    high2 = b // 10**m
    low2 = b % 10**m

    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return z2 * 10**(2*m) + (z1 - z2 - z0) * 10**m + z0


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    with open("input.txt") as f:
        A, B = map(int, f.readline().split())

    result = karatsuba(A, B)

    print(result)
