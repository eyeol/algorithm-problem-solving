import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    triangle = [0]
    for _ in range(N):
        triangle = triangle + list(map(int, input().split()))
    numbers = N * (N + 1) // 2
    dp = [0] * (numbers + 1)
    dp[1] = triangle[1]
    pivot = 2
    count = pivot
    for i in range(2, numbers + 1):
        if count == 0:
            pivot += 1
            count = pivot

        left = pivot - 1
        right = pivot

        if count == pivot:
            dp[i] = dp[i - left] + triangle[i]
        elif count == 1:
            dp[i] = dp[i - right] + triangle[i]
        else:
            dp[i] = max(dp[i - left], dp[i - right]) + triangle[i]

        count -= 1

    print(max(dp))


solution()
