import heapq
import sys

input = sys.stdin.readline

INF = 2000_000

def solution():
    V, E = map(int, input().split())
    start = int(input())

    # padding
    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v,w))
    
    dist = [INF] * (V+1)
    
    dist[start] = 0
    q = [(0, start)]

    while q:
        cur_dist, u = heapq.heappop(q)
        if cur_dist > dist[u]:
            continue
        
        for v, w in adj[u]:
            if dist[v] > cur_dist + w:
                dist[v] = cur_dist + w
                heapq.heappush(q, (dist[v], v))

    for i in range(1, V + 1):
        print("INF" if dist[i] == INF else dist[i])

if __name__ == "__main__":
    solution()
