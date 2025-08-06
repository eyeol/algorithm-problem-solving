import sys

input = sys.stdin.readline


def solution():
    s = input().strip()

    ones = []
    zeros = []

    for i, ch in enumerate(s):
        num = int(ch)
        if num == 1:
            ones.append((1, i))
        else:  # num = 0
            zeros.append((0, i))

    ones = ones[len(ones) // 2 :]
    zeros = zeros[: len(zeros) // 2]

    result = ones + zeros

    result.sort(key=lambda x: x[1])

    out = []
    for re in result:
        out.append(re[0])

    print("".join(map(str, out)))


if __name__ == "__main__":
    solution()
