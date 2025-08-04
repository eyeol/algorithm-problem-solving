import math
import sys

input = sys.stdin.readline


def quad(matrix, r, c, size, out):
    if size == 1:
        out.append(matrix[r][c])
        return
    first = matrix[r][c]
    same = True
    for i in range(r, r + size):  # r에서 r+size-1까지
        row = matrix[i]  # 하나의 row에 대해
        for j in range(c, c + size):
            if row[j] != first:
                same = False
                break
        if not same:
            break
    if same:
        out.append(first)
        return

    h = size // 2
    out.append("(")
    quad(matrix, r, c, h, out)
    quad(matrix, r, c + h, h, out)
    quad(matrix, r + h, c, h, out)
    quad(matrix, r + h, c + h, h, out)
    out.append(")")


def solution():
    N = int(input())
    matrix = [list(input().strip()) for _ in range(N)]
    out = []
    quad(matrix, 0, 0, N, out)
    print("".join(out))


if __name__ == "__main__":
    solution()
