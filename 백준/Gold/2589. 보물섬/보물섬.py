import sys
from collections import deque

input = sys.stdin.readline

DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]

def build_components(maps, H, W):
    comp = [[-1] * W for _ in range(H)]
    comps = []             # 각 컴포넌트의 경계 L 리스트
    sizes = []             # 각 컴포넌트 크기
    cid = 0

    for i in range(H):
        for j in range(W):
            if maps[i][j] == 'L' and comp[i][j] == -1:
                q = deque([(i, j)])
                comp[i][j] = cid
                boundary = []
                size = 0

                while q:
                    x, y = q.popleft()
                    size += 1
                    is_boundary = False

                    for k in range(4):
                        nx, ny = x + DX[k], y + DY[k]
                        if not (0 <= nx < H and 0 <= ny < W) or maps[nx][ny] == 'W':
                            is_boundary = True
                        else:
                            if comp[nx][ny] == -1 and maps[nx][ny] == 'L':
                                comp[nx][ny] = cid
                                q.append((nx, ny))

                    if is_boundary:
                        boundary.append((x, y))

                comps.append(boundary)
                sizes.append(size)
                cid += 1

    return comp, comps, sizes

def bfs_farthest_from(start, cid, maps, H, W, comp, seen, dist, tag):
    tag += 1
    sx, sy = start
    q = deque([(sx, sy)])
    seen[sx][sy] = tag
    dist[sx][sy] = 0
    far = 0

    while q:
        x, y = q.popleft()
        d = dist[x][y]
        if d > far:
            far = d
        for k in range(4):
            nx, ny = x + DX[k], y + DY[k]
            if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] == 'L':
                if comp[nx][ny] == cid and seen[nx][ny] != tag:
                    seen[nx][ny] = tag
                    dist[nx][ny] = d + 1
                    q.append((nx, ny))

    return far, tag

def solution():
    H, W = map(int, input().split())
    maps = [input().strip() for _ in range(H)]

    comp, comps, sizes = build_components(maps, H, W)

    # 재사용 배열 + 스탬프
    seen = [[0] * W for _ in range(H)]
    dist = [[0] * W for _ in range(H)]
    tag = 0

    ans = 0
    for cid, boundary in enumerate(comps):
        # 컴포넌트 자체가 현재 ans를 절대 못 이기면 스킵
        if sizes[cid] - 1 <= ans:
            continue
        if not boundary:  # 고립 1칸 같은 경우
            continue

        for s in boundary:
            far, tag = bfs_farthest_from(s, cid, maps, H, W, comp, seen, dist, tag)
            if far > ans:
                ans = far

    print(ans)

if __name__ == "__main__":
    solution()
