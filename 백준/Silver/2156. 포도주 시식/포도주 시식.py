import sys

input = sys.stdin.readline


def main():
    N = int(input())
    wine = [0]  # 시작점

    for _ in range(N):
        wine.append(int(input()))

    if N == 1:
        print(wine[1])
        return

    if N == 2:
        print(wine[1] + wine[2])
        return

    dp = [0] * (N + 1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    dp[3] = max(wine[1] + wine[3], wine[2] + wine[3], wine[1] + wine[2])

    for i in range(4, N + 1):
        dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 1])

    print((max(dp)))


if __name__ == "__main__":
    main()
