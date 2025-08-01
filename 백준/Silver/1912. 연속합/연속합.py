import sys

input = sys.stdin.readline


def kadane(arr):
    best = curr = arr[0]
    best_start = best_end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if curr + arr[i] < arr[i]:
            curr = arr[i]
            temp_start = i
        else:
            curr += arr[i]

        if curr > best:
            best = curr
            best_start = temp_start
            best_end = i

    return best_start, best_end, best


def solution():
    _ = int(input())
    A = list(map(int, input().split()))

    _, _, result = kadane(A)
    print(result)


solution()
