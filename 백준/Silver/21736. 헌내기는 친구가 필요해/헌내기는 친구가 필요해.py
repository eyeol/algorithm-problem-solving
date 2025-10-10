import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution():
    N, M = map(int, input().split())
    campus = [list(input().strip()) for _ in range(N)]

    # 도연이 위치
    sx, sy = 0, 0
    for i in range(N):
        for j in range(M):
            if campus[i][j] == "I":
                sx, sy = i, j

    visited = [[0 for _ in range(M)] for _ in range(N)]

    def in_range(x, y):
        return 0 <= x < N and 0 <= y < M
    
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    people = 0

    while q:
        x, y = q.popleft()
        if campus[x][y] == "P":
            people += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny]:
                if campus[nx][ny] != "X":
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    print(people if people else "TT")

if __name__ == "__main__":
    solution()
