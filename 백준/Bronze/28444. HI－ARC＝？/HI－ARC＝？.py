import sys

input = sys.stdin.readline

def solution():
    h, i, a, r, c = map(int, input().split())

    first = h * i
    second = a * r * c
    result = first - second

    print(result)

if __name__ == "__main__":
    solution()