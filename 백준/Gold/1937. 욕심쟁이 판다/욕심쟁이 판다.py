import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solution():
    N = int(input())

    forest = [list(map(int, input().split())) for _ in range(N)]
    # x, y는 0부터 N-1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 함수 안에서 dp table을 사용해야 할 것 같은데
    dp = [[0]*N for _ in range(N)]

    # 새로운 시작점에 대해 함수 호출하기 전에 visited 초기화
    def get_optimal_sol(x, y):
        if dp[x][y]:
            return dp[x][y]

        optimal = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and forest[nx][ny] > forest[x][y]:
                optimal = max(optimal, 1 + get_optimal_sol(nx, ny))
        dp[x][y] = optimal
        return optimal

    ans = max(get_optimal_sol(i, j) for i in range(N) for j in range(N))

    print(ans)


if __name__ == "__main__":
    solution()
