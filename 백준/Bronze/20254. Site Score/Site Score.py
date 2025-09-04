import sys

input = sys.stdin.readline

def solution():
    ur, tr, uo, to = map(int, input().split())

    print(56*ur + 24*tr + 14*uo + 6*to)


if __name__ == "__main__":
    solution()