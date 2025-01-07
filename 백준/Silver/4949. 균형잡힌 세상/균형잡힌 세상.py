def is_balanced(seq: str):
    flag_stack = []

    for token in seq:
        if token == "(":
            flag_stack.append("(")
        elif token == ")":
            if flag_stack and flag_stack[-1] == "(":
                flag_stack.pop()
            else:
                return False
        elif token == "[":
            flag_stack.append("[")
        elif token == "]":
            if flag_stack and flag_stack[-1] == "[":
                flag_stack.pop()
            else:
                return False

    return not flag_stack


def solution():
    seq = "init"
    while True:
        seq = input()

        if seq == ".":
            break
        is_balance = is_balanced(seq)

        if is_balance:
            print("yes")
        else:
            print("no")


solution()
