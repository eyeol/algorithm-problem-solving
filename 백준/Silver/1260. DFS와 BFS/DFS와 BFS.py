import sys
input = sys.stdin.readline

def dfs(graph, visited, now, result):
    visited[now] = True
    result.append(str(now))

    for neighbor in graph[now]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor, result)

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True
    l, r = 0, 1
    result = []

    while l < r:
        node = queue[l]
        l += 1
        result.append(str(node))
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                r += 1

    return result

def solution():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for edges in graph:
        edges.sort()

    visited = [False] * (N + 1)
    dfs_result = []
    dfs(graph, visited, V, dfs_result)
    print(" ".join(dfs_result))

    # 🔧 visited 재초기화 필요!
    visited = [False] * (N + 1)
    bfs_result = bfs(graph, V)
    print(" ".join(bfs_result))

solution()
