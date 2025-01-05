import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_x, start_y, graph):
    n, m = len(graph), len(graph[0])
    distance = [[-1 if graph[i][j] != 0 else 0 for j in range(m)] for i in range(n)]
    distance[start_x][start_y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    return distance


def find_start(jido, n, m):
    for i in range(n):
        for j in range(m):
            if jido[i][j] == 2:
                return i, j


def solution():
    # n : 세로, m : 가로
    n, m = map(int, input().split())

    jido = [list(map(int, input().split())) for _ in range(n)]
    start_x, start_y = find_start(jido, n, m)

    distance = bfs(start_x, start_y, jido)

    for row in distance:
        print(*row)


solution()
