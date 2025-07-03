import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    tri = [list(map(int, input().split())) for _ in range(N)]

    dp = tri[0][:]

    for i in range(1, N):
        nxt = [0] * (i + 1)

        nxt[0] = dp[0] + tri[i][0]
        nxt[-1] = dp[-1] + tri[i][i]

        for j in range(1, i):
            nxt[j] = max(dp[j - 1], dp[j]) + tri[i][j]

        dp = nxt

    print(max(dp))


solution()
