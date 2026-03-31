BRACKETS = {
    ")": "(", "]": "[", "}" : "{"
}

def solve(array):
    stack = []
    for i in array:
        if i in BRACKETS.values():
            stack.append(i)
        else:
            if len(stack) == 0:
                print("no")
                return
            else:
                if stack.pop() != BRACKETS[i]:
                    print("no")
                    return
    if len(stack) == 0:
        print("yes")
        return
    else:
        print("no")
        return

if __name__ == "__main__":

    seq = input().strip()
    solve(seq)