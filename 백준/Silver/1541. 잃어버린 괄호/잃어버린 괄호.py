import sys

input = sys.stdin.readline

# Given
# Mathemathical Expression

# Goal
# maximize result


def solution():
    expr = input().strip()
    groups = expr.split("-")

    results = []
    for g in groups:
        results.append(sum(map(int, g.split("+"))))

    result = results[0]

    for i in range(1, len(results)):
        result -= results[i]

    print(result)


if __name__ == "__main__":
    solution()
