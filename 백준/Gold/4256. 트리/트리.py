import sys

input = sys.stdin.readline

# Given
# 이진 트리 문제
# 모든 노드는 최대 2개의 자식 노드 가질 수 있음
# 왼쪽 자식이 순서 먼저
# n개의 노드로 이루어진 이진 트리를 BT라고 하자
# 노드는 1부터 n까지 distinct한 번호가 있음
# 순회 방법; 전위, 중위, 후위
# 전위 순회, 중위 순회한 결과가 주어짐

# Goal
# 두 순회 결과를 가지고 다시 BT를 만들 수 있음
# 그래서 후위 순회 결과를 구해야 함


# 뭔가 재귀적으로 풀면 될 것 같음


def solution():
    T = int(input())
    result = []
    for _ in range(T):
        # node 개수
        N = int(input())

        pre = list(map(int, input().split()))
        ino = list(map(int, input().split()))

        # 중위 순회 결과에서, 노드의 인덱스를 가리키는 해시 테이블 작성
        pos = {v: i for i, v in enumerate(ino)}
        # 전위 결과에서 (서브)트리의 인덱스를 가리킬 인덱스
        post = []
        pre_idx = 0

        def dfs(inL, inR):
            nonlocal pre_idx
            # base case
            if inL > inR:
                return
            # 가장 처음에 pre[0]이 전체 트리의 루트
            root = pre[pre_idx]
            pre_idx += 1  # 무슨 근거로 1을 더하지
            # 중위 순회 결과 상에서 루트의 위치를 기준으로 inL, inR을 나눔
            mid = pos[root]

            dfs(inL, mid - 1)
            dfs(mid + 1, inR)
            post.append(root)

        dfs(0, N - 1)
        result.append(" ".join(map(str, post)))

    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    solution()
