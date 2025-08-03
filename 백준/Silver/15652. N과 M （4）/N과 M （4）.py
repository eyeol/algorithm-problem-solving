import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    numbers = list(range(1, N + 1))
    for i in combinations_with_replacement(numbers, M):
        print(*i)


solution()
