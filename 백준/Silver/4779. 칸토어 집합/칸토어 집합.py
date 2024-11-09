import sys


def cantor(N):
    if N == 0:
        return "-"
    child = cantor(N - 1)

    return child + " " * (3 ** (N - 1)) + child


def sol():
    for line in sys.stdin:
        N = int(line.strip())
        print(cantor(N))


sol()
