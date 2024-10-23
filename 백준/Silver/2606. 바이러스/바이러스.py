from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                
    return count

# 입력 받기
n = int(input())  # 컴퓨터의 수 (노드 수)
m = int(input())  # 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수 (엣지 수)

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 네트워크 연결 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부를 기록할 배열
visited = [False] * (n + 1)

# 1번 컴퓨터가 감염되었을 때 감염된 컴퓨터의 수 (1번 컴퓨터 제외)
infected_count = bfs(1, graph, visited) - 1

print(infected_count)
