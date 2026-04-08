def get_priority(op):
    if op in '+-': return 1
    if op in '*/': return 2
    return 3


def solve():
    expr = input().strip()
    stack = []

    for char in reversed(expr):
        if char.isalpha():
            stack.append((char, 3))
        else:
            op1_val, op1_prec = stack.pop()
            op2_val, op2_prec = stack.pop()

            curr_prec = get_priority(char)

            left = op1_val
            if op1_prec < curr_prec:
                left = f"({op1_val})"

            right = op2_val
            if op2_prec < curr_prec or (op2_prec == curr_prec and char in "-/"):
                right = f"({op2_val})"

            new_val = f"{left}{char}{right}"
            stack.append((new_val, curr_prec))

    print(stack[0][0])


solve()