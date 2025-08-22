import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.read

# Given
# 이진 탐색 트리
# 전위 순회 결과가 주어짐

# Goal
# 이 트리를 후위 순회한 결과

# How to solve
# 전위 순회 첫번째 결과가 트리 루트
# 그 다음 트리보다 큰 값이 나올 때까지 left, 큰 값이 나오면 그 뒤는 전부 right
# 후위 순회 결과를 출력하려면
# left - right - root 순서


def solution():
    # str으로 받을 땐 strip() 붙여주는게 안전
    pre = list(map(int, input().strip().split("\n")))

    lo = 0
    hi = len(pre)  # N

    def DivideConquer(lo, hi):
        # 리프 노드에 도달하면 키값 출력
        if lo >= hi:
            return

        root = pre[lo]
        # 어디까지가 left이고 right인지 알고 싶음
        pivot = hi
        for i in range(lo + 1, hi):  # 1부터 N-1
            if pre[i] > root:
                pivot = i
                break
        # left
        DivideConquer(lo + 1, pivot)
        # right
        DivideConquer(pivot, hi)
        print(root)

    DivideConquer(lo, hi)


if __name__ == "__main__":
    solution()
