import sys
from collections import deque

input = sys.stdin.readline


def bfs(N, K):
    global time

    visited = set()
    queue = deque([(N, 0)])

    while queue:
        current, time = queue.popleft()

        if current == K:
            return time

        if current not in visited:
            visited.add(current)

            if current - 1 >= 0:
                queue.append((current - 1, time + 1))
            if current + 1 <= 100000:
                queue.append((current + 1, time + 1))
            if current * 2 <= 100000:
                queue.append((current * 2, time + 1))


def solution():
    N, K = map(int, input().split())
    result = bfs(N, K)

    print(result)


solution()
