import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())

    subjects = [(0, 0)] # padding

    # (중요도, 공부 시간)
    for _ in range(K):
        v, t = map(int, input().split())
        subjects.append((v, t))

    # row : item 개수(수업 개수)
    # col : item 무게(여기서는 수강 시간)
    # element : 가치(여기서는 중요도)
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

    for i in range(1, K+1): # 1에서 K
        value, time = subjects[i]
        for j in range(1, N+1):
            if j >= time:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + value)
            else:
                dp[i][j] = dp[i-1][j]
    
    print(dp[K][N])



if __name__ == "__main__":
    solution()
