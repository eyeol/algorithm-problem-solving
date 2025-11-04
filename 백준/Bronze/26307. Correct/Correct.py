import sys

input = sys.stdin.readline


def solution():
    HH, MM = map(int, input().split())

    ans = (HH - 9)*60 + MM

    print(ans)

if __name__ == "__main__":
    solution()
