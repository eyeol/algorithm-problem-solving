import sys

input = sys.stdin.readline


def solution():
    # N X N 행렬, M : testcase 수
    N, M = map(int, input().split())

    board = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        board.append(arr)

    sum_board = [[0] * N for _ in range(N)]
    summation_x = 0
    summation_y = 0
    for i in range(N):
        summation_x += board[0][i]
        summation_y += board[i][0]
        sum_board[0][i] = summation_x
        sum_board[i][0] = summation_y

    for i in range(1, N):
        for j in range(1, N):
            sum_board[i][j] = (
                sum_board[i][j - 1]
                + sum_board[i - 1][j]
                - sum_board[i - 1][j - 1]
                + board[i][j]
            )

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        result = sum_board[x2][y2]
        if x1 > 0:
            result -= sum_board[x1 - 1][y2]
        if y1 > 0:
            result -= sum_board[x2][y1 - 1]
        if x1 > 0 and y1 > 0:
            result += sum_board[x1 - 1][y1 - 1]
        print(result)


solution()
