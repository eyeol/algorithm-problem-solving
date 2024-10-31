T = int(input())

for i in range(T):
    R, S = (input().split())
    R = int(R)
    output = ""
    for cr in S:
        output += (cr*R)
    print(output)