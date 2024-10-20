T = int(input())


for i in range(T):

    PS = input().strip()

    valid = True
    up_down = 0

    for char in PS:
        # 중간에 음수가 되면 그 즉시 invalid로 판단
        if up_down < 0:
            valid = False
            break
        if char == "(":
            up_down += 1
        else:
            up_down -= 1

    if up_down != 0:
        valid = False

    if valid:
        print("YES")
    else:
        print("NO")
