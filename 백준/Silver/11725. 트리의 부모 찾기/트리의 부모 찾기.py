import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N = int(input())
    adj = [[] for i in range(0, N + 1)]
    for _ in range(1, N):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    parent = [0] * (N + 1)
    q = deque([1])  # root
    parent[1] = -1

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if parent[nxt] == 0:
                parent[nxt] = cur
                q.append(nxt)

    print("\n".join(map(str, parent[2:])))


solution()
