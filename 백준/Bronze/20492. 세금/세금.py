import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# Given
# 제세공과금에 대한 정보
# 전체 금액의 22%를 국가에 납부, 나머지를 수령
# 하지만 상금의 80%를 필요 경비로 인정하게 되면,
# 나머지 20% 중 22%만을 제세공과금으로 납부해도 됨

# Goal
# 각각의 경우 수령하는 상금을 알아보자
# 78%
# 80 + 15.6 = 95.6


def solution():
    N = int(input())

    f_ans = (N * 78) // 100
    s_ans = (N * 956) // 1000

    print(f"{f_ans} {s_ans}")


if __name__ == "__main__":
    solution()
