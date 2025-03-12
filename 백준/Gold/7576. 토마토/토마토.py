import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력


def count_date(storage):
    date = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()

    N = len(storage)
    M = len(storage[0])

    for i in range(N):
        for j in range(M):
            if storage[i][j] == 1:
                queue.append((i, j, 0))  # (행, 열, 날짜)

    while queue:
        x, y, day = queue.popleft()
        date = max(date, day)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and storage[nx][ny] == 0:
                storage[nx][ny] = 1
                queue.append((nx, ny, day + 1))

    for row in storage:
        if 0 in row:
            return -1  # 익지 않은 토마토가 있으면 -1 반환

    return date


def solution():
    M, N = map(int, input().split())
    storage = [list(map(int, input().split())) for _ in range(N)]
    print(count_date(storage))


solution()
