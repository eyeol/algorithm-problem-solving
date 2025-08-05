import sys

input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(a + b)


solution()
