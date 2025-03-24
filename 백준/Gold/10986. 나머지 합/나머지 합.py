import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # P = []
    remain = [0] * M
    prefix = 0
    for number in A:
        prefix += number
        # P.append(prefix)
        remain[prefix % M] += 1

    count = 0
    for i in range(M):
        candidate = remain[i]
        satisfied = candidate * (candidate - 1) / 2
        count += int(satisfied)
    count += remain[0]

    print(count)


solution()
