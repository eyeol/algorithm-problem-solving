import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    numbers = list(map(int, input().split()))
    target = int(input())

    count = 0
    for number in numbers:
        if number == target:
            count += 1

    print(count)


solution()
