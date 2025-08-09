import heapq
import sys

input = sys.stdin.readline

# Given
# 절댓값 힙 규칙
# 절대값이 가장 작은 값 출력, 절대값이 가장 작은 값이 여러개일 때는 가장 작은 수를 출력
# 그러니까 음수를 출력하라는 뜻


def solution():
    N = int(input())
    heap = []

    for _ in range(N):
        x = int(input())

        if x == 0:
            if not heap:
                print("0")
            else:
                out = heapq.heappop(heap)
                print(out[1])
        else:
            heapq.heappush(heap, (abs(x), x))


if __name__ == "__main__":
    solution()
