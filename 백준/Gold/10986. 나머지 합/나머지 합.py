import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    P = []
    remain = []
    prefix = 0
    for number in A:
        prefix += number
        P.append(prefix)
        remain.append(prefix % M)

    count = 0
    for i in range(M):
        candidate = remain.count(i)
        satisfied = candidate * (candidate - 1) / 2
        count += int(satisfied)
    count += remain.count(0)

    print(count)


solution()
