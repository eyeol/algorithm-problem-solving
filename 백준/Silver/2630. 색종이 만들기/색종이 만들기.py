import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0


def dfs(x, y, size):
    global blue, white
    whole = size**2
    count = 0
    count += sum(sum(row[y : y + size]) for row in board[x : x + size])
    if whole == count:
        blue += 1
    elif count == 0:
        white += 1
    else:
        dfs(x, y, size // 2)
        if (x + size // 2) in range(N) and (y + size // 2) in range(N):
            dfs(x, y + size // 2, size // 2)
            dfs(x + size // 2, y, size // 2)
            dfs(x + size // 2, y + size // 2, size // 2)


def solution():
    dfs(0, 0, N)
    print(white)
    print(blue)


solution()
