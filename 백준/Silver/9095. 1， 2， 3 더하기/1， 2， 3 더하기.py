import sys

input = sys.stdin.readline

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):  # 4부터 10까지
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N <= 0:
            print(0)
        else:
            print(dp[N])


if __name__ == "__main__":
    main()
