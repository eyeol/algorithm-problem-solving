import sys

input = sys.stdin.readline

# anchor : 맨 왼쪽, 맨 위
# search_points : anchor를 포함한 4개의 점

N, c, r = map(int, input().split())


def z_search(n, x, y):
    if n == 0:
        return 0

    half = 2 ** (n - 1)

    if c < x + half and r < y + half:
        return z_search(n - 1, x, y)
    elif c < x + half and r >= y + half:
        return half * half + z_search(n - 1, x, y + half)  # 2번 사분면
    elif c >= x + half and r < y + half:
        return 2 * half * half + z_search(n - 1, x + half, y)  # 3번 사분면
    else:
        return 3 * half * half + z_search(n - 1, x + half, y + half)  # 4번 사분면


def solution():
    print(z_search(N, 0, 0))


solution()
