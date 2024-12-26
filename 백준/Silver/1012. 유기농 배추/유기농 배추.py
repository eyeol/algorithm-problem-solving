import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(x, y):
    visited[x][y] = 1
    for tx, ty in steps:
        nx, ny = x + tx, y + ty
        if nx in range(M) and ny in range(N) and not visited[nx][ny] and board[nx][ny]:
            dfs(nx, ny)


def sol():

    count = 0
    for x in range(M):
        for y in range(N):
            if board[x][y] and not visited[x][y]:
                dfs(x, y)
                count += 1
    print(count)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[False for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = True

    sol()
