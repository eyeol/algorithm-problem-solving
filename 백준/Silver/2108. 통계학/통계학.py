import sys
from collections import Counter

input = sys.stdin.readline


def solution():
    N = int(input())
    numbers = []
    sum = 0
    for _ in range(N):
        x = int(input())
        sum += x
        numbers.append(x)

    sorted_numbers = sorted(numbers)

    aver = sum / N
    middle = sorted_numbers[len(sorted_numbers) // 2]

    freq_count = Counter(numbers)
    most_common = freq_count.most_common()
    most_common.sort(key=lambda x: (-x[1], x[0]))

    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        many = most_common[1][0]  
    else:
        many = most_common[0][0]

    maximum = sorted_numbers[-1] - sorted_numbers[0]

    print(int(round(aver, 0)))
    print(middle)
    print(many)
    print(maximum)


solution()
