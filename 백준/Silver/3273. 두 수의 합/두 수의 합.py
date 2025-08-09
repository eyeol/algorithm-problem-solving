import sys

input = sys.stdin.readline

# Given
# n개의 서로 다른 양의 정수로 이루어진 수열
# 1 이상 100만 이하

# Goal
# 자연수 x가 주어졌을 때, ai + aj = x를 만족하는 ai aj 쌍의 수

# How to solve
# n이 100만이라서 n log n 하면 딱 2000만 (파이썬 1초)
#


def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    X = int(input())

    arr.sort()

    # 투 포인터 세팅
    l = 0
    r = N - 1

    cnt = 0

    while l < r:
        sum = arr[l] + arr[r]

        if sum == X:
            cnt += 1
            l += 1
            r -= 1
        elif sum < X:
            l += 1
        else:  # sum > X
            r -= 1

    print(cnt)


if __name__ == "__main__":
    solution()
