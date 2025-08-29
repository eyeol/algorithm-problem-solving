import sys

input = sys.stdin.readline


def main():
    s, k, h = map(int, input().split())

    if s + k + h >= 100:
        print("OK")
    else:
        min = s
        target = "Soongsil"
        if k < min:
            min = k
            target = "Korea"
        if h < min:
            target = "Hanyang"
        print(target)


if __name__ == "__main__":
    main()
