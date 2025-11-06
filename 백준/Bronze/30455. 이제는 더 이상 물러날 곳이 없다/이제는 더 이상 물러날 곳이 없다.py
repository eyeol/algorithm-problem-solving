import sys

input = sys.stdin.readline


def solution():
    num = int(input())

    if num % 2 == 0:
        print("Duck")
    else:
        print("Goose")

if __name__ == "__main__":
    solution()
