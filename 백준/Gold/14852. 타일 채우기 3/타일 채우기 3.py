import sys

input = sys.stdin.readline

MOD = 1_000_000_007


def solution():
    N = int(input())
    d = [0] * 1000001

    d[0] = 1
    d[1] = 2
    d[2] = 7

    if N <= 2:
        print(d[N])
    else:
        prefix = 2 * d[0]
        for i in range(3, N + 1):
            d[i] = 2 * d[i - 1] + d[i - 2]
            prefix += 2 * d[i - 2]
            d[i] += prefix
            d[i] %= MOD

        # Memoization
        ans = d[N]
        print(ans)


solution()
