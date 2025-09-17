import heapq
import sys

input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        K = int(input())
        chapters = [0] + list(map(int, input().split()))
        ps = [0]*(K+1)
        for i in range(1, K+1):
            ps[i] = ps[i-1] + chapters[i]
        
        INF = 10**18
        dp = [[0]*(K+1) for _ in range(K+1)]

        for L in range(2, K+1):
            for i in range(1, K-L+2):
                j = i + L - 1
                s = ps[j] - ps[i-1]
                best = INF

                for k in range(i, j):
                    best = min(best, dp[i][k] + dp[k+1][j] + s)
                dp[i][j] = best
        
        print(dp[1][K])

if __name__ == "__main__":
    solution()
