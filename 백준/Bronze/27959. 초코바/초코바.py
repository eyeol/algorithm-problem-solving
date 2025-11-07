import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    if N*100 >= M:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solution()
