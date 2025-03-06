import sys

input = sys.stdin.readline


def solution():
    scores = []
    for _ in range(5):
        scores.append(int(input().strip()))
    print(sum(scores))


solution()
