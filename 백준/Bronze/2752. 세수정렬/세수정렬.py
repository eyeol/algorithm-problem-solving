import sys

input = sys.stdin.readline


def insertion_sort(numbers: list):
    N = len(numbers)

    for i in range(1, N):  # 1 ~ N-1
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


def solution():
    numbers = list(map(int, input().split()))
    insertion_sort(numbers)

    print(" ".join(map(str, numbers)))


solution()
