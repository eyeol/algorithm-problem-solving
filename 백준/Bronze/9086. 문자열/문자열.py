import sys

input = sys.stdin.readline


def solution():
    T = int(input().strip())
    for _ in range(T):
        testcase = input().strip()
        start = testcase[0]
        end = testcase[-1]
        print(start + end)


solution()
