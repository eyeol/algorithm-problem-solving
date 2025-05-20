import sys
from collections import deque

input = sys.stdin.readline

dfs_result = []
bfs_result = []


def dfs(node: int):
    if visited[node]:
        return

    visited[node] = 1
    dfs_result.append(node)
    for i in adj[node]:
        dfs(i)


def bfs(node: int):
    deq = deque([node])

    while deq:
        out = deq.popleft()
        if not visited[out]:
            visited[out] = 1
            bfs_result.append(out)
            for i in adj[out]:
                if not visited[i]:
                    deq.append(i)


def solution():
    N, M, V = map(int, input().split())
    global adj
    adj = [[] for _ in range(N + 1)]

    global visited
    visited = [0] * (N + 1)
    for _ in range(M):
        i, j = map(int, input().split())
        # undirected graph
        adj[i].append(j)
        adj[j].append(i)
    for i in range(1, N + 1):
        adj[i].sort()

    dfs(V)
    visited = [0] * (N + 1)
    bfs(V)
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))


solution()
