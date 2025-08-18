import sys
from collections import deque

input = sys.stdin.readline

# Given
# 재현이가 잘못된 수를 부르면 0을 외쳐서 쓴 수를 지우게 함

# Goal
# 모든 수 받아적은 후 합을 알고 싶음

# How to solve
# 가장 최근에 쓴 수를 지우는거라서 후입선출 = 스택 사용


def solution():
    K = int(input())
    stacks = []
    for _ in range(K):
        x = int(input())
        if x == 0:
            stacks.pop()
        else:
            stacks.append(x)

    print(sum(stacks))


if __name__ == "__main__":
    solution()
