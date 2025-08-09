import sys

input = sys.stdin.readline

MAX_HEIGHT = 1_000_000_000


# O(N); N이 100만이라 괜찮음
def get_wood(trees: list, height: int):
    s = 0
    for tree in trees:
        if tree > height:
            s += tree - height
    return s


def solution():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    lo, hi = 0, MAX_HEIGHT
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if get_wood(trees, mid) >= M:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)


if __name__ == "__main__":
    solution()
