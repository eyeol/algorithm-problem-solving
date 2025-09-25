import sys

input = sys.stdin.readline

# 1000을 1000번 더한 값보다 크도록
INF = 1000_000_000

def solution():
    N = int(input())

    house = [[INF, INF, INF]]
    # N x 3 행렬 생성
    for _ in range(N):
        house.append(list(map(int, input().split())))

    result = []

    for color in range(3): # color = 0, 1, 2
        # 인덱스 : 1부터 N
        dp = [[[INF, INF, INF] for _ in range(3)] for _ in range(N+1)] # 1부터 N

        # 첫번째는 R색을 골랐다고 가정하고 2번째 집을 색칠
        c1 = (color + 1) % 3
        c2 = (color + 2) % 3
        for j in range(3):
            for k in range(3):
                # dp[2][0]는 그대로 INF, INF, INF
                # 첫번째 집 빨간색으로 칠한 비용 + 현재 위치 비용
                dp[2][c1][k] = house[1][color] + house[2][c1] # g로 칠함
                dp[2][c2][k] = house[1][color] + house[2][c2] # b로 칠함
        
        #print(dp[2])

        for i in range(3, N): # 3부터 N-1까지
            # RGB별로
            for j in range(3):
                prev = dp[i-1]

                # 이번 집은 빨간색이야
                if j == 0:
                    # dp[i][j][j]는 그대로 INF
                    # 1은 G에서 가져온 것 중 최소
                    dp[i][j][1] = min(prev[1]) + house[i][j]
                    dp[i][j][2] = min(prev[2]) + house[i][j]
                elif j == 1:
                    dp[i][j][0] = min(prev[0]) + house[i][j]
                    dp[i][j][2] = min(prev[2]) + house[i][j]
                else: # j == 2
                    dp[i][j][0] = min(prev[0]) + house[i][j]
                    dp[i][j][1] = min(prev[1]) + house[i][j]
            
            #print(dp[i])
        
        # 마지막 집은 빨간색으로 칠하면 안됨
        for j in range(3):
            prev = dp[N-1]

            if j == color: # 빨간색은 패스
                pass
            elif j == c1:
                dp[N][j][color] = min(prev[color]) + house[N][j]
                dp[N][j][c2] = min(prev[c2]) + house[N][j]
            elif j == c2: # j == 2
                dp[N][j][color] = min(prev[color]) + house[N][j]
                dp[N][j][c1] = min(prev[c1]) + house[N][j]

        result.append(dp[N])

    #print(result)
    minimum = INF

    for dp_n in result:
        for col in dp_n:
            for v in col:
                if v < minimum:
                    minimum = v

    print(minimum)

if __name__ == "__main__":
    solution()
