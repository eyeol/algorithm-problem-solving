import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    cost = []
    for _ in range(N):
        # 0 : R, 1 : G, 2; B
        cost.append(list(map(int, input().split())))
    dp = [[0] * 3 for _ in range(N)]
    # 초기값은 첫번째 방 비용
    dp[0] = cost[0]
    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    print(min(dp[N - 1]))


solution()
