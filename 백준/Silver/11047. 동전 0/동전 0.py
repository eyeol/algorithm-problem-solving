import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]

    count = 0
    for coin in coins[::-1]:
        count += K // coin
        K = K % coin

    print(count)


solution()
