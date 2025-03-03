import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    for i in range(N):
        print("*" * (N - i))


solution()
