import sys

input = sys.stdin.readline


def FindMaxCrossingSubarray(A, low, mid, high):
    left_sum = A[mid]
    sum = A[mid]
    left_end = mid
    for i in range(mid - 1, low - 1, -1):  # low까지 내려감
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            left_end = i

    right_sum = A[mid + 1]
    sum = A[mid + 1]
    right_end = mid + 1
    for i in range(mid + 2, high + 1):  # high까지 올라감
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            right_end = i

    return left_end, right_end, left_sum + right_sum


def FindMaxSubarray(A, low, high):
    if low == high:
        return low, high, A[low]

    else:
        mid = (low + high) // 2
        left_low, left_high, left_max = FindMaxSubarray(A, low, mid)
        right_low, right_high, right_max = FindMaxSubarray(A, mid + 1, high)
        cross_low, cross_high, cross_max = FindMaxCrossingSubarray(A, low, mid, high)
        if left_max >= right_max and left_max >= cross_max:
            return left_low, left_high, left_max
        elif right_max >= left_max and right_max >= cross_max:
            return right_low, right_high, right_max
        else:
            return cross_low, cross_high, cross_max


def solution():
    T = int(input())

    for _ in range(T):
        N = int(input())
        array = list(map(int, input().split()))
        le, ri, maximum = FindMaxSubarray(array, 0, N - 1)
        print(maximum)


solution()
