import sys
from collections import deque

input = sys.stdin.readline

# Given
# 리프 노드; 자식의 개수가 0인 노드
# 트리가 주어졌을 때, 노드 하나를 지울 것
# 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거

# Goal
# 그때 트리에 남은 리프 노드의 개수를 구하는 것

# How to solve
# 지울 노드는 한개 주어짐
# 부모가 없는 노드는 루트 하나
# 리프 노드는 누군가의 부모가 아닌 노드
# 그러면 parent 리스트에 없는 노드
# 0 1 2 3 4
# 에서 2가 지워짐
# 원래 리프노드는 2, 3, 4였다가 3,4 2개가 남게 됨
# 이것도 큐다
# 어떤 노드가 사라짐
# 그 노드가 부모인 값들을 찾아서
# 큐에 넣음
# 그 큐들도 하나씩 사라짐
# 그 큐를 부모로 가지는 값들도 사라짐
# 부모가 사라진다는건 -1이 된다는것
# parent의 모든 값이 -1이 되면 루트만 남는거니까 1을 출력
# 큐에서 어떤 작업으로 parent를 바꿀지?
# 일단 적어보자


def solution():
    N = int(input())
    parents = list(map(int, input().split()))
    target = int(input())

    # 루트를 골라버리면 0개
    if parents[target] == -1:
        print(0)
        return

    # 삭제할 노드
    q = deque([target])
    while q:
        out = q.popleft()
        parents[out] = -1
        for i, node in enumerate(parents):
            # 부모가 삭제될 노드이면
            if node == out:
                # 삭제할 노드에 추가
                q.append(i)

    # 리프 노드는 어떻게 알지?
    # 일단 부모가 있어야 함
    # 그리고 나를 부모로 가지는 노드가 없어야 함
    np_cnt = 0
    lv_cnt = 0
    for i, node in enumerate(parents):
        if node == -1:
            np_cnt += 1
        else:  # node != -1
            if i not in parents:
                lv_cnt += 1
    if np_cnt == N:
        print(1)
    else:
        print(lv_cnt)


if __name__ == "__main__":
    solution()
