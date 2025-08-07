import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    words = []

    for _ in range(N):
        word = input().strip()
        words.append((word, len(word)))

    words = list(set(words))
    words.sort(key=lambda x: (x[1], x[0]))

    for word in words:
        print(word[0])


if __name__ == "__main__":
    solution()
