import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solution():
    N = int(input())

    forest = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cells = []
    for i in range(N):
        for j in range(N):
            cells.append((forest[i][j], i, j))

    cells.sort(reverse=True)

    dp = [[1]*N for _ in range(N)]

    for val, x, y in cells:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and forest[nx][ny] < val:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)
    
    ans = max(max(row) for row in dp)

    print(ans)


if __name__ == "__main__":
    solution()
