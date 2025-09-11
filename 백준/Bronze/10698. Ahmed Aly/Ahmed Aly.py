T = int(input())

for case in range(1, T + 1):
    eq = list(input().split("="))
    left = eval(eq[0])
    right = int(eq[1])
    if left == right:
        print(f"Case {case}: YES")
    else:
        print(f"Case {case}: NO")
