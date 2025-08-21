import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# Given
# 이진 트리의 중위, 후위가 주어짐

# Goal
# 전위 탐색 결과 출력

# How to solve
# inorder가 있어야 분할 정복으로 풀 수 있음
# postorder는 분할 기준 위치를 찾는 용도


def solution():
    N = int(input())
    ino = list(map(int, input().split()))
    post = list(map(int, input().split()))

    # 중위 탐색에서 노드의 인덱스
    hash = {v: i for i, v in enumerate(ino)}

    result = []
    # 후위에서 루트인 노드값을 찾는다
    # 그 노드값이 중위 결과에서 어느 위치인지 본다
    # 그 위치를 기준으로 분할 정복을 한다
    # 레츠고

    # 초기 루트 인덱스는 가장 마지막
    r_idx = -1

    def dfs(inL, inR, r_idx):
        if inL > inR:
            return
        # hash[r_idx]가 중위에서의 루트의 위치 ; 3 = 왼쪽 노드 수
        # 전체 노드 수에서 왼쪽 노드 수를 빼면, 오른쪽 노드 수

        # post에서 sub tree의 root 정보 가져옴
        mid = post[r_idx]
        # 중위 결과 상에서 root값의 위치를 찾음
        mid_idx = hash[mid]

        nxt_r_idx = r_idx - 1
        nxt_l_idx = r_idx - 1 - (inR - mid_idx)

        # 전위 결과 ; root - left - right
        result.append(mid)
        dfs(inL, mid_idx - 1, nxt_l_idx)
        dfs(mid_idx + 1, inR, nxt_r_idx)

    dfs(0, N - 1, r_idx)

    print(*result)


if __name__ == "__main__":
    solution()
