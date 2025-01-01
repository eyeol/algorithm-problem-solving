import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))


def search_height(l, r):
    target_height = 0

    while l <= r:
        h = (l + r) // 2
        wood_cutted = sum(tree - h if tree > h else 0 for tree in trees)

        if wood_cutted >= M:
            target_height = h
            l = h + 1
        else:
            r = h - 1

    return target_height


def solution():

    minimum = 0
    maximum = max(trees)
    result = search_height(minimum, maximum)
    print(result)


solution()
