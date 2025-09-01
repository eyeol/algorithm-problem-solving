import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    dp = [0] * (k+1)
    dp[0] = 1

    for c in coins:
        for i in range(c, k+1): # c부터 k까지
            dp[i] += dp[i-c] # i-c는 0부터 k-c까지

    print(dp[k])


if __name__ == "__main__":
    solution()
