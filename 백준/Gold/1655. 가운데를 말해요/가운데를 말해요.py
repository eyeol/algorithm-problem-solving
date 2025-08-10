import heapq
import sys

input = sys.stdin.readline

# Goal
# 정수 하나 외칠 때, 이떄까지 말한 수 중에서 중간값을 말해야 함
# 짝수개면, 가운데 2개 중에 작은 값


def solution():
    N = int(input())
    left_heap = []
    right_heap = []

    for _ in range(N):
        x = int(input())
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -x)
        else:
            heapq.heappush(right_heap, x)

        if right_heap and -left_heap[0] > right_heap[0]:
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
            heapq.heappush(right_heap, -heapq.heappop(left_heap))

        print(-left_heap[0])


if __name__ == "__main__":
    solution()
