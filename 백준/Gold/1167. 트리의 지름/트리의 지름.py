import sys

sys.setrecursionlimit(200_000)

input = sys.stdin.readline


def dfs(node: int, dist: int):
    visited[node] = 1
    far_node, far_dist = node, dist
    for nxt, w in graph[node]:
        if not visited[nxt]:
            cand_node, cand_dist = dfs(nxt, dist + w)
            if cand_dist > far_dist:
                far_node, far_dist = cand_node, cand_dist
    return far_node, far_dist


def solution():
    V = int(input())
    global graph, visited

    graph = [[] for i in range(V + 1)]
    for _ in range(V):
        info = list(map(int, input().split()))
        v = info[0]
        i = 1
        while info[i] != -1:
            u, w = info[i], info[i + 1]
            graph[v].append((u, w))
            graph[u].append((v, w))
            i += 2

    visited = [False] * (V + 1)
    A, _ = dfs(1, 0)
    visited = [False] * (V + 1)
    _, diameter = dfs(A, 0)

    print(diameter)


solution()
