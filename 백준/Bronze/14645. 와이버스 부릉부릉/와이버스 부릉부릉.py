import sys

input = sys.stdin.readline


def main():
    N, _ = map(int, input().split())
    for _ in range(N):
        _, _ = map(int, input().split())
    print("비와이")


if __name__ == "__main__":
    main()
