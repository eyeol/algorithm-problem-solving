import sys

input = sys.stdin.readline


def main():
    N = int(input())

    S = input().strip()

    print(S[-5:])


if __name__ == "__main__":
    main()
