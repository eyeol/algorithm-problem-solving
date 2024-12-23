import sys

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)


def dfs(cur):

    for i in range(1, N + 1):
        if adj[cur][i] == 1:
            if visited[i] == 1:
                pass
            else:
                visited[i] = 1
                dfs(i)


def sol():
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1

    count = 0

    for i in range(1, N + 1):
        if visited[i] != 1:
            count += 1
            dfs(i)
    print(count)


sol()
