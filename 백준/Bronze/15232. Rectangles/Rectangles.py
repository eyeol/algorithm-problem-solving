import sys

input = sys.stdin.readline


def solution():
    r = int(input())
    c = int(input())

    ans = "*"*c
    for _ in range(r):
        print(ans)

if __name__ == "__main__":
    solution()
