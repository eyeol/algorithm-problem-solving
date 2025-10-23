import sys

input = sys.stdin.readline

def solution():
    a, b, c = map(int, input().split())

    if a+b == c:
        print("correct!")
    else:
        print("wrong!")


if __name__ == "__main__":
    solution()
