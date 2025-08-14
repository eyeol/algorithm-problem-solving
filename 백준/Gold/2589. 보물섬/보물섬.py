import sys
from collections import deque

input = sys.stdin.readline

# Given
# 보물섬 지도는 2차원 행렬 형태
# 지도의 각 칸은 육지(L)나 바다(W)로 표시
# 상하좌우 이웃한 육지로만 이동 가능
# 한 칸 이동하는데 한 시간
# 보물은 서로 최단 거리로 이동하는데 있어
# 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻힘
# 육지를 나타내는 두 곳 사이 최단 거리 이동하려면, 같은 곳 두번 이상 지나거나 멀리 돌아가면 안됨

# Goal
# 보물이 묻힌 두 곳의 최단 거리로 이동하는 시간을 구하고 싶음

# How to solve
# 보물 묻힌 두 곳을 어떻게 특정하지?
# 최단 거리로 가도 가장 오래 걸리는 곳
# 그런데 도달 가능해야 함
# visited  활용해서 최대 시간 체크

DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def bfs(maps: list, h: int, w: int, sx: int, sy: int):
    dist = [[-1] * w for _ in range(h)]
    deq = deque([(sx, sy)])

    dist[sx][sy] = 0
    far = 0

    while deq:
        x, y = deq.popleft()
        d = dist[x][y]
        if d > far:
            far = d
        for i in range(4):
            nx, ny = x + DX[i], y + DY[i]
            if (
                0 <= nx < h
                and 0 <= ny < w
                and maps[nx][ny] == "L"
                and dist[nx][ny] == -1
            ):
                dist[nx][ny] = d + 1
                deq.append((nx, ny))

    return far


def solution():
    h, w = map(int, input().split())
    maps = [input().strip() for _ in range(h)]

    ans = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == "L":
                ans = max(ans, bfs(maps, h, w, i, j))

    print(ans)


if __name__ == "__main__":
    solution()
