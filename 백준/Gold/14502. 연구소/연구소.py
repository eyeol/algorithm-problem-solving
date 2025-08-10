import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# Given
# 연구소 크기 N X M
# 일부 칸은 바이러스가 존재, 상하좌우
# 새로 세울 수 있는 벽의 개수는 3개, 꼭 3개를 모두 세워야 함
# 0은 빈칸, 1은 벽, 2는 바이러스(허거덩)

# Goal
# 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 함
# 안전 영역의 크기의 최대값을 구하는 프로그램

# How to solve
# 벽을 세울 위치 3개를 어떻게 찾지
# 경우의 수 나눠보자
# 아니 바둑처럼 감싸는걸 어떻게 알아
# 그냥 0인 애들 중에 3개 고르나?
# 그래놓고 BFS 해서 안전 영역 최대 되는걸 고르는?


Dx = [1, -1, 0, 0]
Dy = [0, 0, 1, -1]


def bfs(tmp, virus, N, M):
    q = deque(virus)
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + Dx[k], cy + Dy[k]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))
    safe = 0
    for i in range(N):
        safe += tmp[i].count(0)
    return safe


def solution():
    N, M = map(int, input().split())

    maps = [list(map(int, input().split())) for _ in range(N)]

    virus = []
    blank = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                blank.append((i, j))
            elif maps[i][j] == 2:
                virus.append((i, j))

    ans = 0

    for w1, w2, w3 in combinations(blank, 3):
        tmp = [row[:] for row in maps]
        tmp[w1[0]][w1[1]] = 1
        tmp[w2[0]][w2[1]] = 1
        tmp[w3[0]][w3[1]] = 1

        safe = bfs(tmp, virus, N, M)
        if safe > ans:
            ans = safe

    print(ans)


if __name__ == "__main__":
    solution()
