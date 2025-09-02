import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    sentence = list(input().split())

    for word in sentence:
        print(word, "DORO", sep="", end=" ")
if __name__ == "__main__":
    solution()
