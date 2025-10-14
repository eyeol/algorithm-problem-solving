import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())

    if N == K:
        print(0)
        print(N)
        return
    
    MAX = 100000
    # 최단거리
    dist = [-1] * (MAX + 1)
    # 역추적용 리스트
    parent = [-1] * (MAX + 1)

    q = deque([N])
    dist[N] = 0

    while q:
        x = q.popleft()
        if x == K:
            break

        nxts = [x-1, x+1, 2*x]
        for nx in nxts:
            if 0 <= nx <= MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                parent[nx] = x
                q.append(nx)

    path = []
    cur = K
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    
    path.reverse()

    print(dist[K])
    print(*path)

if __name__ == "__main__":
    solution()
