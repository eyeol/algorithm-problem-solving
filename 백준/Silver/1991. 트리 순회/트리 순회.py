import sys

input = sys.stdin.readline

# Given
# 트리 입력 받음

# Goal
# 전위 순회
# 중위 순회
# 후위 순회 결과 출력

# How to solve
# 인접 리스트처럼 그래프를 정리해야하나
# 파이썬 딕셔너리로 해보자


def preorder(T: dict, node: str, result: list):  # 트리와 루트를 받음
    if node == ".":
        return
    left, right = T[node]
    result.append(node)
    preorder(T, left, result)
    preorder(T, right, result)


def inorder(T: dict, node: str, result: list):  # 트리와 루트를 받음
    if node == ".":
        return
    left, right = T[node]
    inorder(T, left, result)
    result.append(node)
    inorder(T, right, result)


def postorder(T: dict, node: str, result: list):  # 트리와 루트를 받음
    if node == ".":
        return
    left, right = T[node]
    postorder(T, left, result)
    postorder(T, right, result)
    result.append(node)


def solution():
    N = int(input())
    nodes = {}
    root, l, r = input().split()
    nodes[root] = (l, r)
    nodes["."] = "NIL"
    for _ in range(N - 1):
        p, l, r = input().split()
        nodes[p] = [l, r]
    # .이면 NIL

    # pre
    result = []
    preorder(nodes, root, result)
    print("".join(result))

    # in
    result = []
    inorder(nodes, root, result)
    print("".join(result))

    # post
    result = []
    postorder(nodes, root, result)
    print("".join(result))


if __name__ == "__main__":
    solution()
