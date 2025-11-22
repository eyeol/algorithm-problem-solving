import sys
from collections import deque

input = sys.stdin.readline

# 정점이 적어서 Adj Matrix로 표현 (최대 10000개)
# 각 점마다 bfs 돌림

def solution():
    N = int(input())

    adj = [list(map(int, input().split())) for _ in range(N)]
    
    ans = [[0 for _ in range(N)] for _ in range(N)]

    
    
    for s in range(N):
        visited = [0] * N
        q = deque([s])

        while q:
            cur = q.popleft()
            for nxt, edge in enumerate(adj[cur]):
                if edge and not visited[nxt]:
                    visited[nxt] = 1
                    ans[s][nxt] = 1
                    q.append(nxt)
    
    for row in ans:
        print(*row)


if __name__ == "__main__":
    solution() 
