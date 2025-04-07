import sys
from collections import deque

input = sys.stdin.readline


def merge_sort(numbers):
    # base case : 길이가 1이면 그 자체를 반환
    if len(numbers) <= 1:
        return numbers, 0

    # 그게 아니면 오른쪽, 왼쪽 포인터를 비교
    middle = int(len(numbers) // 2)
    left, left_count = merge_sort(numbers[:middle])
    right, right_count = merge_sort(numbers[middle:])

    merged = []
    swap_count = left_count + right_count

    left = deque(left)
    right = deque(right)

    while left and right:
        if left[0] <= right[0]:
            merged.append(left.popleft())
        else:
            merged.append(right.popleft())
            swap_count += len(left)

    merged.extend(left)
    merged.extend(right)

    return merged, swap_count


def solution():
    _ = int(input())
    numbers = list(map(int, input().split()))
    _, ans = merge_sort(numbers)
    print(ans)


solution()
