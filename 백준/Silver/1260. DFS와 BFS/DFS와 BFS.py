import sys
from collections import deque

input = sys.stdin.readline

# 일단 인접 행렬로 풀어보고
# 그 다음 인접 리스트로 풀자

dfs_result = []
bfs_result = []


def dfs(node: int):
    if not visited_dfs[node]:
        visited_dfs[node] = 1
        dfs_result.append(node)
        for i, connected in enumerate(adj[node]):
            if connected:
                dfs(i)
    else:
        return


def bfs(node: int):
    deq = deque([node])

    while deq:
        out = deq.popleft()
        if not visited_bfs[out]:
            visited_bfs[out] = 1
            bfs_result.append(out)
            for i, connected in enumerate(adj[out]):
                if connected:
                    deq.append(i)


def solution():
    N, M, V = map(int, input().split())
    global adj
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    global visited_dfs
    global visited_bfs
    visited_dfs = [0] * (N + 1)
    visited_bfs = [0] * (N + 1)
    for _ in range(M):
        i, j = map(int, input().split())
        # undirected graph
        adj[i][j] = 1
        adj[j][i] = 1

    dfs(V)
    bfs(V)
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))


solution()
