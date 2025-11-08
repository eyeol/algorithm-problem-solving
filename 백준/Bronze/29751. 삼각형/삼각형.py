import sys

input = sys.stdin.readline


def solution():
    W, H = map(int, input().split())
    print(W*H/2)

if __name__ == "__main__":
    solution()
