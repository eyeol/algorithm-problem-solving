import sys

sys.setrecursionlimit(3000)
input = sys.stdin.readline

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

def solution():

    def dfs(graph: list):
        h = len(graph)
        w = len(graph[0])
        
        def in_range(x, y):
            return 0 <= x < h and 0 <= y < w

        visited = [[0 for _ in range(w)] for _ in range(h)]

        def dfs_visit(x, y):
            visited[x][y] = 1
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny]:
                    dfs_visit(nx, ny)

        cnt = 0
        # source마다 재귀함수 호출
        for i in range(h):
            for j in range(w):
                if not visited[i][j] and graph[i][j]:
                    cnt += 1
                    dfs_visit(i, j)

        return cnt

    def dfs_visit(graph, visited, x, y, cnt):
        h = len(graph)
        w = len(graph[0])
        # 육지면 지도에 하나 추가
        visited[x][y] = 1

        def in_range(x, y):
            return 0 <= x < h and 0 <= y < w

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny]:
                dfs_visit(graph, visited, nx, ny, cnt)

        return cnt

    while True:        
        w, h = map(int, input().split())
        # 종료 조건
        if w == 0 and h == 0:
            break
        
        # 지도
        jido = []
        for _ in range(h):
            jido.append(list(map(int, input().split())))
        
        ans = dfs(jido)
        print(ans)


if __name__ == "__main__":
    solution()
