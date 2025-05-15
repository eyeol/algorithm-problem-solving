import sys

input = sys.stdin.readline


def comb(arr, n):
    result = []

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1 :], n - 1):
                result.append([arr[i]] + j)

    return result


def solution():
    N, M = map(int, input().split())

    numbers = list(range(1, N + 1))  # 1 ~ N
    results = comb(numbers, M)

    for result in results:
        print(" ".join(map(str, result)))


solution()
