import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    if M <= 2:
        print("NEWBIE!")
    elif M <= N:
        print("OLDBIE!")
    else:
        print("TLE!")


if __name__ == "__main__":
    main()
