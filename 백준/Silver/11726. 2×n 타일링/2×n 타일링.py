import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1000
dp[0] = 1
dp[1] = 2

for i in range(2, len(dp)):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n - 1] % 10007)
