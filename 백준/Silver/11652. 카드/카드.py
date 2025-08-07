import sys

input = sys.stdin.readline

# Given
# N개의 카드
# 각각의 카드에 정수 적혀있음

# Goal
# 가장 많이 가지고 있는 정수
# 정수가 여러개면 작은 것 출력


def solution():
    N = int(input())
    cards = {}

    for _ in range(N):
        num = int(input())
        if num in cards:
            cards[num] += 1
        else:
            cards[num] = 1

    max_values = max(cards.values())
    max_keys = [k for k, v in cards.items() if v == max_values]

    ans = min(max_keys)

    print(ans)


if __name__ == "__main__":
    solution()
