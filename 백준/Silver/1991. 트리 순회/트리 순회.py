import sys

input = sys.stdin.readline
write = sys.stdout.write


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
    nodes["."] = "NIL"

    for _ in range(N):
        p, l, r = input().split()
        nodes[p] = [l, r]
    # .이면 NIL

    # pre
    result = []
    preorder(nodes, "A", result)
    write("".join(result) + "\n")

    # in
    result = []
    inorder(nodes, "A", result)
    write("".join(result) + "\n")

    # post
    result = []
    postorder(nodes, "A", result)
    write("".join(result) + "\n")


if __name__ == "__main__":
    solution()
