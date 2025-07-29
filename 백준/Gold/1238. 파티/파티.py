import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(adj, start):
    distances = [0] + [INF] * (len(adj) - 1)
    visit = [0] * len(adj)

    distances[start] = 0
    visit[start] = 1

    q = []
    heapq.heappush(q, (distances[start], start))

    while q:
        curr_dist, current = heapq.heappop(q)
        visit[current] = 1
        for next_dist, next in adj[current]:
            if ((curr_dist + next_dist) < distances[next]) and not visit[next]:
                distances[next] = curr_dist + next_dist
                heapq.heappush(q, (distances[next], next))

    return distances


def solution():
    N, M, X = map(int, input().split())

    adj = [[] for _ in range(N + 1)]
    adj_reverse = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, time = map(int, input().split())
        adj[start].append((time, end))
        adj_reverse[end].append((time, start))

    results_1 = dijkstra(adj, X)
    # 진짜 X에서 각각 마을로 가는 최단거리
    results_2 = dijkstra(adj_reverse, X)
    # 모든 시작점에서 X로 가는 최단거리

    final_results = []
    for i in range(1, N + 1):
        final_results.append(results_1[i] + results_2[i])

    print(max(final_results))


solution()
