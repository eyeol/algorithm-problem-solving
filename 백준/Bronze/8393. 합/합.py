import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    result = 0
    while N > 0:
        result += N
        N -= 1

    print(result)


solution()
