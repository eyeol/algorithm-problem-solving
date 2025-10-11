import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution():
    N, M = map(int, input().split())

    miro = [list(map(int, input().strip())) for _ in range(N)]

    q = deque([(0, 0)])


    def in_range(x, y):
        return 0 <= x < N and 0 <= y < M

    while q:
        cx , cy = q.popleft()
        
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if in_range(nx, ny):
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[cx][cy] + 1
                    q.append((nx, ny))

    print(miro[N-1][M-1])


if __name__ == "__main__":
    solution()
