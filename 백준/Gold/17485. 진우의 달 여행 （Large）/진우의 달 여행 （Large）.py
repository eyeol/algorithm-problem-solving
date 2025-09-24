import sys

input = sys.stdin.readline

# 1000을 1000번 더한 값보다 크도록
INF = 1000_000_000

def solution():
    N, M = map(int, input().split())

    space = []
    # N x M 행렬 생성
    for _ in range(N):
        space.append(list(map(int, input().split())))
    
    # 동일한 사이즈의 dp table
    dp = [[[INF, INF, INF] for _ in range(M)] for _ in range(N)]

    for j in range(M):
        for i, v in enumerate(dp[0][j]):
            dp[0][j][i] = space[0][j]
    

    for i in range(1, N): # 1부터 N-1
        for j in range(M): # 0부터 M-1
            prev = dp[i-1]
            left = -1
            right = M
            
            if j-1 >= 0:
                left = j-1
            if j+1 < M:
                right = j+1

            # left가 범위에 있으면
            if left >= 0:
                lmin_fuel = min(prev[left][1], prev[left][2])
                dp[i][j][0] = space[i][j] + lmin_fuel
            
            # right가 범위에 있으면
            if right < M:
                rmin_fuel = min(prev[right][0], prev[right][1])
                dp[i][j][2] = space[i][j] + rmin_fuel
            
            cmin_fuel = min(prev[j][0], prev[j][2])
            dp[i][j][1] = space[i][j] + cmin_fuel
    
    minimum = INF
    for j in range(M):
        for k in range(3):
            if dp[N-1][j][k] < minimum:
                minimum = dp[N-1][j][k]
    
    print(minimum)

if __name__ == "__main__":
    solution()
