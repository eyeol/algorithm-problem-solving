import heapq
import sys

input = sys.stdin.readline

# Given
# 카드 합체 놀이
# 자연수가 쓰여진 n장의 카드
# i번째 카드에는 ai가 쓰여있음

# 카드 합체 규칙
# x번 카드와 y번 카드를 골라 두 장에 쓰여진 수를 더한 값을 계산
# 계산한 값을 x번 카드와 y번 카드에 덮어쓴다

# 이 카드 합체를 m번 하면 놀이가 끝남
# m번 합체 후, n장의 카드에 쓰여있는 수를 모두 더한 값이 이 놀이의 점수
# 점수를 가장 작게 만드는게 놀이의 목표


def solution():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    # 일단 min heap으로 만든다 (점수를 작게 해야 하니까)
    heapq.heapify(cards)

    for _ in range(M):
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)

        s = a + b

        heapq.heappush(cards, s)
        heapq.heappush(cards, s)

    print(sum(cards))


if __name__ == "__main__":
    solution()
