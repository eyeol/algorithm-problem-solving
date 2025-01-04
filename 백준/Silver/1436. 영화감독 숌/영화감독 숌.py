import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    count = 1
    number = 666
    while count < N:
        number += 1
        if "666" in str(number):
            count += 1
    print(number)


solution()
