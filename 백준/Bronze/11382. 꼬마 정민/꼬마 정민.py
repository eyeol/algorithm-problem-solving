import sys

input = sys.stdin.readline


def solution():
    a, b, c = map(int, input().split())

    print(a + b + c)


if __name__ == "__main__":
    solution()
