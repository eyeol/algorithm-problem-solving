import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    remain = [0] * M
    prefix = 0
    for number in A:
        prefix += number
        remain[prefix % M] += 1

    ans = remain[0]
    for i in range(M):
        ans += (remain[i] * (remain[i] - 1)) // 2

    print(ans)


solution()
