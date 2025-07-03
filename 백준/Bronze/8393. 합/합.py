import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    result = N * (N + 1) // 2

    print(result)


solution()
