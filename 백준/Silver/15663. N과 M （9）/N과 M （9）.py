import sys
from itertools import permutations

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    result = list(permutations(a, M))
    result = list(set(result))
    result.sort()
    for comb in result:
        print(" ".join(map(str, comb)))


solution()
