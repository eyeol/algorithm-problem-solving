import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    for _ in range(N):
        a, b, x = map(int, input().split())
        w = a*(x-1) + b
        print(w)

if __name__ == "__main__":
    solution()
