import sys

input = sys.stdin.readline


def lcs(X: str, Y: str):
    m, n = len(X), len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        xi = X[i - 1]
        for j in range(1, n + 1):
            if xi == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c[m][n]


def solution():
    X = input().strip()
    Y = input().strip()

    print(lcs(X, Y))


solution()
