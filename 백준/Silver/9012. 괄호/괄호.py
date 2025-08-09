import sys

input = sys.stdin.readline

# Given
# Valid PS 정보

# Goal
# 주어진 문자열에 대해 VPS인지 아닌지 determine

# How to solve
# 이건 스택/큐/힙 문제인데 어떤걸 사용해야 하는지 생각해보자


def determine(ps: str):
    cnt = 0
    for ch in ps:
        if ch == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return "NO"
    if cnt != 0:
        return "NO"
    return "YES"


def solution():
    T = int(input())

    for _ in range(T):
        ps = input().strip()

        print(determine(ps))


if __name__ == "__main__":
    solution()
