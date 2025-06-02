import sys

input = sys.stdin.readline


def dp(d, x: int):
    if x == 1:
        return 1
    if x == 2:
        return 3
    if d[x] != 0:
        return d[x]
    d[x] = (dp(d, x - 1) + 2 * dp(d, x - 2)) % 10007
    return d[x]


def solution():
    N = int(input())
    d = [0] * 1001

    # Memoization
    ans = dp(d, N)
    print(ans)


solution()
