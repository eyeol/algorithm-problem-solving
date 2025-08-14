import heapq
import sys

input = sys.stdin.readline

# Given
# 소설을 여러 장으로 나누어 쓰는 중
# 각 장은 각각 다른 파일에 저장
# 소설의 모든 장 다 쓰면, 각 장이 쓰여진 파일 합쳐서 한개의 파일로 만든다
# 이 과정에서 2개의 파일 합쳐서 하나의 임시 파일 만들고
# 이 임시 파일이나 원래 파일을 계속 2개씩 합쳐서 최종적으로 하나로 만든다
# 두개의 파일 합칠 때 필요한 비용은 두 파일 크기의 합

# Goal
# 필요한 비용의 총합
# 정확히는 최소 비용

# 저번에 풀었던 문제랑 완전 동일한 문제


def solution():
    T = int(input())
    for _ in range(T):
        # 소설의 장 수는 풀이에 필요x
        _ = int(input())
        novel = list(map(int, input().split()))
        # n logn
        heapq.heapify(novel)

        total = 0
        while len(novel) > 1:
            a = heapq.heappop(novel)
            b = heapq.heappop(novel)

            s = a + b
            total += s

            heapq.heappush(novel, s)

        print(total)


if __name__ == "__main__":
    solution()
