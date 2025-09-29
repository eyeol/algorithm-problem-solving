import sys

input = sys.stdin.readline


def solution():
    x = input().strip()
    y = input().strip()

    M = len(x)
    N = len(y)

    cur = [0] * (N+1)
    ans = 0

    # row major
    for i in range(1, M+1): # 1부터 M
        nxt = [0] * (N+1)
        for j in range(1, N+1): # 1부터 N
            if x[i-1] == y[j-1]:
                nxt[j] = cur[j-1] + 1
                ans = max(ans, nxt[j])
        cur = nxt
    
    print(ans)

if __name__ == "__main__":
    solution()
