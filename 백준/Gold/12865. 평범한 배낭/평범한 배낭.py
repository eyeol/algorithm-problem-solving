import sys

input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())

    items = []
    for _ in range(N):
        w, v = map(int, input().split())
        if w <= K:
            items.append((w, v))

    # tabulation
    dp = [0] * (K+1)

    for w, v in items:
        for k in range(K, w-1, -1): # K에서 w까지
            dp[k] = max(dp[k], dp[k-w] + v)
    
    print(dp[K])



if __name__ == "__main__":
    solution()
