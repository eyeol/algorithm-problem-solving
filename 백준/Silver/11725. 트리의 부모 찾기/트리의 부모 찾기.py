import sys
from collections import deque

def solution():
    input = sys.stdin.buffer.readline
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    parent = [0] * (N + 1) 
    parent[1] = -1         

    q = deque([1])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if parent[nxt] == 0:  
                parent[nxt] = cur
                q.append(nxt)

    out = "\n".join(map(str, parent[2:]))
    sys.stdout.write(out)

if __name__ == "__main__":
    solution()
