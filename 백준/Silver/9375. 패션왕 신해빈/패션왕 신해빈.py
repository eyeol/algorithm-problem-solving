import sys

input = sys.stdin.readline


def solution():
    T = int(input().strip())

    for _ in range(T):
        N = int(input().strip())
        commode = {}
        for _ in range(N):
            cloth, kind = input().split()
            if kind in commode:
                commode[kind].append(cloth)
            else:
                commode[kind] = [cloth]
        keys = [*commode]
        ans = 1
        for key in keys:
            ans = ans * (len(commode[key]) + 1)
        ans = ans - 1
        print(ans)


solution()
