import sys

input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())

    # 1 - A/B = B/B - A/B = (B-A)/B
    print(b-a, b)


if __name__ == "__main__":
    solution()
