import sys
from decimal import ROUND_HALF_UP, Decimal

input = sys.stdin.readline


def round_half_up(n):
    return int(Decimal(n).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def solution():
    N = int(input())
    opinions = []
    for _ in range(N):
        opinions.append(int(input()))
    opinions.sort()
    if N:
        margin = round_half_up(len(opinions) * 0.15)
        start = margin
        end = len(opinions) - margin
        trimmed_mean = round_half_up(sum(opinions[start:end]) / (end - start))
        print(trimmed_mean)
    else:
        print(0)


solution()
