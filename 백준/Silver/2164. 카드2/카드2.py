import sys
from collections import deque

input = sys.stdin.readline

# Given
# N장의 카드, 각각 1부터 N까지 번호가 붙어있음
# 1번이 제일 위, N번이 제일 아래

# 카드가 한장 남을 때까지 다음 동작 반복
# 제일 위에 있는 카드 버린다
# 그 다음 제일 위에 있는 카드를 제일 아래 카드 밑으로 옮긴다

# Goal
# 마지막 남는 카드

# How to solve
# popleft를 해야하니까 deque를 쓰자


def solution():
    N = int(input())

    cards = deque(range(1, N + 1))  # 1부터 N 들어있음

    while len(cards) > 1:
        cards.popleft()
        top = cards.popleft()
        cards.append(top)

    print(cards[0])


if __name__ == "__main__":
    solution()
