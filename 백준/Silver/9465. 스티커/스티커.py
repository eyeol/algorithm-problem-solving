import sys

input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        stickers = [list(map(int, input().split())) for _ in range(2)]
        if N == 1:
            print(max(stickers[0][0], stickers[1][0]))
            continue
        dp = [[0] * N for _ in range(2)]

        dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
        dp[0][1], dp[1][1] = dp[1][0] + stickers[0][1], dp[0][0] + stickers[1][1]


        for i in range(2, N):  # 2 to N-1
            candi1 = dp[0][i - 1] + stickers[1][i]
            candi2 = dp[1][i - 1] + stickers[0][i]

            candi3 = dp[0][i - 2] + stickers[1][i]
            candi4 = dp[1][i - 2] + stickers[0][i]

            dp[0][i] = max(candi2, candi4)
            dp[1][i] = max(candi1, candi3)

        candi1 = dp[0][N - 1]
        candi2 = dp[0][N - 2]
        candi3 = dp[1][N - 1]
        candi4 = dp[1][N - 2]

        print(max(candi1, candi2, candi3, candi4))


solution()
