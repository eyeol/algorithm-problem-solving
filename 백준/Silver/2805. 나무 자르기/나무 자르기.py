import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    lo, hi = 0, max(trees)
    ans = 0

    while lo <= hi:
        # H 역할
        mid = (lo + hi) // 2
        s = 0
        for t in trees:
            if t > mid:
                s += t - mid
                if s >= M:
                    break
        if s >= M:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)


if __name__ == "__main__":
    solution()
