import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    d = [0] * 31

    d[0] = 1
    d[2] = 3
    d[4] = 11
    for i in range(6, 31):  # 6 ~ 30
        d[i] = 3 * d[i - 2]
        j = i - 4
        while j >= 0:
            d[i] += 2 * d[j]
            j -= 2

    # Memoization
    ans = d[N]
    print(ans)


solution()
