import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
add = 0
dp = [0] * len(numbers)
for i in range(len(numbers)):
    add += numbers[i]
    dp[i] += add

dp.insert(0, 0)

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[end]-dp[start - 1])
