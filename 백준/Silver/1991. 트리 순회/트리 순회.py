import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder_traversal(node: Node, res: str):
    if node is None:
        return
    res.append(node.data)
    preorder_traversal(node.left, res)
    preorder_traversal(node.right, res)


def inorder_traversal(node: Node, res: str):
    if node is None:
        return
    inorder_traversal(node.left, res)
    res.append(node.data)
    inorder_traversal(node.right, res)


def postorder_traversal(node: Node, res: str):
    if node is None:
        return
    postorder_traversal(node.left, res)
    postorder_traversal(node.right, res)
    res.append(node.data)


def solution():
    N = int(input())
    nodes = {}
    for _ in range(N):
        data, left, right = map(str, input().split())

        if data not in nodes:
            nodes[data] = Node(data)
        cur = nodes[data]

        if left != ".":
            if left not in nodes:
                nodes[left] = Node(left)
            cur.left = nodes[left]

        if right != ".":
            if right not in nodes:
                nodes[right] = Node(right)
            cur.right = nodes[right]

    root = nodes["A"]

    res = []
    preorder_traversal(root, res)
    print("".join(res))

    res = []
    inorder_traversal(root, res)
    print("".join(res))

    res = []
    postorder_traversal(root, res)
    print("".join(res))


solution()
