import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    board = []
    sum_board = []
    for _ in range(N):
        # 일반 배열
        arr = list(map(int, input().split()))
        # 합 배열
        sum_arr = []
        summation = 0
        for num in arr:
            summation += num
            sum_arr.append(summation)
        board.append(arr)
        sum_board.append(sum_arr)
    for i in range(M):
        result = 0
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(x1 - 1, x2):  # x1-1에서 x2-1까지
            if y1 > 1:
                result += sum_board[j][y2 - 1] - sum_board[j][y1 - 2]
            else:
                result += sum_board[j][y2 - 1]
        print(result)


solution()
