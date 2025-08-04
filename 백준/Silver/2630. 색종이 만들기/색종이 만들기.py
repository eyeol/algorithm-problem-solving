import sys

input = sys.stdin.readline


def Cut(paper, r, c, size, record):
    # Base Case
    if size == 1:
        if paper[r][c] == 0:
            record[0] += 1
            return
        else:
            record[1] += 1
            return

    first = paper[r][c]
    same = True

    for i in range(r, r + size):
        row = paper[i]
        for j in range(c, c + size):
            if row[j] != first:
                same = False
                break
        if same is False:
            break
    if same is True:
        if first == 0:
            record[0] += 1
            return
        else:
            record[1] += 1
            return

    h = size // 2
    Cut(paper, r, c, h, record)
    Cut(paper, r, c + h, h, record)
    Cut(paper, r + h, c, h, record)
    Cut(paper, r + h, c + h, h, record)

    return


def solution():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    record = [0, 0]
    Cut(paper, 0, 0, N, record)

    print(record[0])
    print(record[1])


if __name__ == "__main__":
    solution()
