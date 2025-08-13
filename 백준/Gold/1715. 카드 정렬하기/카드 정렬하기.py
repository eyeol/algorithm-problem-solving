import heapq
import sys

input = sys.stdin.readline

# Given
# 정렬된 두 묶음의 숫자 카드
# 두 묶음을 합쳐서 하나로 만드는데 A+B번 비교를 해야 함

# 여러 묶음이 있는데, 먼저 묶으면 나중에 중복으로 카운팅됨
# 그러니까 처음에 무조건 갯수가 적은 묶음을 합치는게 이득

# Goal
# N개의 숫자 카드 묶음의 각각 크기가 주어졌을 때
# 최소 몇번의 비교가 필요한지


def solution():
    N = int(input())
    heap = []
    # min heap
    for _ in range(N):
        heapq.heappush(heap, int(input()))

    # base case
    if N <= 1:
        print(0)
        return

    ans = 0
    # 힙에 하나만 남을 때까지
    # 하나가 되었다는건 모든 비교를 다했다는 뜻
    while len(heap) > 1:
        # 가장 작은 2개를 뺀다
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        s = a + b
        ans += s
        heapq.heappush(heap, s)

    print(ans)


if __name__ == "__main__":
    solution()
