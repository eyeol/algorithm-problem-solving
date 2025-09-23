import sys

input = sys.stdin.readline


def solution():
    a, b, c = map(int, input().split())

    one = int(a*b/c)
    two = int(a/b*c)

    print(max(one, two))



if __name__ == "__main__":
    solution()
