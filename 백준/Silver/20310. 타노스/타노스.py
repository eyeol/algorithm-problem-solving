import sys

input = sys.stdin.readline


def solution():
    s = input().strip()

    zeros = []
    ones = []

    for ch in s:
        num = int(ch)
        if num == 1:
            ones.append(num)
        else:  # num = 0
            zeros.append(num)

    zeros = zeros[: len(zeros) // 2]
    ones = ones[: len(ones) // 2]

    result = sorted(zeros + ones)

    print("".join(map(str, result)))


if __name__ == "__main__":
    solution()
