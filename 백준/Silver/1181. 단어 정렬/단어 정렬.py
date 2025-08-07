import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    words = [(input().strip()) for _ in range(N)]

    words = list(set(words))
    words.sort(key=lambda x: (len(x), x))

    print("\n".join(words))


if __name__ == "__main__":
    solution()
