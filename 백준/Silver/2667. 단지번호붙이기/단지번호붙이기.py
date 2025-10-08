import heapq
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution():
    N = int(input())

    # row는 string 형태
    # index로 접근 가능
    jido = [list(map(int, input().strip())) for _ in range(N)]

    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    def in_range(x, y):
        return 0 <= x < N and 0 <= y < N

    # recursive하게?
    def get_danji(x, y):
        visited[x][y] = 1
        size = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and not visited[nx][ny] and jido[nx][ny] == 1:
                size += get_danji(nx, ny)
        
        return size

    sizes = []
    for i in range(N):
        for j in range(N):
            if jido[i][j] == 1 and not visited[i][j]:
                sizes.append(get_danji(i, j))

    sizes.sort()
    print(len(sizes))
    for size in sizes:
        print(size)

if __name__ == "__main__":
    solution()
