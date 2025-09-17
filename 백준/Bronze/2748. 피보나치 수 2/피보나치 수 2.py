import sys

input = sys.stdin.readline

# Given
# 피보나치 수
# n은 90 이하 자연수

# Goal
# n번째 피보나치 구하기


def solution():
    dp = [0] * 91
    dp[1] = 1

    for i in range(2, 91):
        dp[i] = dp[i-1] + dp[i-2]
    
    n = int(input())

    print(dp[n])


if __name__ == "__main__":
    solution()
