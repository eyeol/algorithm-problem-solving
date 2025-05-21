import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]

    count = 0
    opt = 0
    while K > 0:
        for coin in reversed(coins):
            if coin <= K:
                opt = coin
                break
        count += K // opt
        K = K % opt

    print(count)


solution()
