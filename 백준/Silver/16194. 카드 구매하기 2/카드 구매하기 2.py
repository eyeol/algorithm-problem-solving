import sys

input = sys.stdin.readline

# Given
# 카드 등급 8개
# 카드팩은 카드 1개가 포함된, ... , 카드 N개가 포함된 총 N가지가 존재

# Goal
# 돈을 최소로 지불해서 카드 N개를 구매하려고 함
# 민규가 지불해야 하는 금액의 최소값
# 딱 N개를 사야 함


def solution():
    N = int(input())
    P = [0] + list(map(int, input().split()))

    INF = 10**15
    dp = [INF] * (N+1)
    dp[0] = 0

    for i in range(1, N+1):  # 2부터 N
        for j in range(1, i+1):  # 1부터 i
            dp[i] = min(dp[i], dp[i-j] + P[j])

    print(dp[N])


if __name__ == "__main__":
    solution()
