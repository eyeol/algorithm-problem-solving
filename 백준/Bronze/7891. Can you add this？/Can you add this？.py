import sys

input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        print(x + y)


if __name__ == "__main__":
    solution()
