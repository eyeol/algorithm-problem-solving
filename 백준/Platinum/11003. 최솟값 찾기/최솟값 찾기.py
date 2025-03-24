import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, L = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    D = [0] * (N + 1)

    dq = deque()

    for i in range(1, 1 + N):  # 1 ~ N

        while dq and A[dq[-1]] > A[i]:
            dq.pop()

        dq.append(i)

        if dq[0] <= i - L:
            dq.popleft()

        D[i] = str(A[dq[0]])

    print(" ".join(D[1:]))


solution()
