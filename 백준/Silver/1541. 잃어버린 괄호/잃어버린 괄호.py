import sys
import re

input = sys.stdin.readline


def solution():
    expr = input().strip()

    parts = expr.split("-")

    result = sum(map(int, parts[0].split("+")))

    for part in parts[1:]:
        result -= sum(map(int, part.split("+")))

    print(result)


solution()
