import sys

input = sys.stdin.readline


def solution():
    a = input().strip()
    b = input().strip()
    c = input().strip()

    A, B, C = len(a), len(b), len(c)

    dp = [[[0] * (C + 1) for _ in range(B + 1)] for __ in range(A + 1)]

    for i in range(1, A+1):
        for j in range(1, B+1):
            for k in range(1, C+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    print(dp[A][B][C])

if __name__ == "__main__":
    solution()
