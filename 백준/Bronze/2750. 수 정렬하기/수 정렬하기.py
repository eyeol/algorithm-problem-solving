import sys

input = sys.stdin.readline


def quick_sort(numbers: list, lo=0, hi=None):
    if hi is None:
        hi = len(numbers) - 1

    if lo >= hi:
        return

    pivot = numbers[lo]
    left = lo + 1
    right = hi

    while True:
        while left <= right and numbers[left] <= pivot:
            left += 1
        while left <= right and numbers[right] >= pivot:
            right -= 1
        if left >= right:
            break

        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1

    # 교차 후
    numbers[lo], numbers[right] = numbers[right], numbers[lo]

    quick_sort(numbers, lo, right - 1)
    quick_sort(numbers, right + 1, hi)


def solution():
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))
    quick_sort(numbers)

    print("\n".join(map(str, numbers)))


solution()
