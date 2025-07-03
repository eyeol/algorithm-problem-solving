import sys

input = sys.stdin.readline


def solution():
    A, B, C = map(int, (input().split()))
    print(pow(A, B, C))


solution()
