import sys
from itertools import permutations

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    for result in list(permutations(numbers, M)):
        print(" ".join(map(str, result)))


solution()
