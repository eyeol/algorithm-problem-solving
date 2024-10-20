M, N = map(int, input().split())

large_board = []

for i in range(M):
    large_board.append(input())

# 맨 왼쪽 위가 정해지면 나머지 채색도 같이 정해진다

# 그러면 맨 왼쪽 위를 기준으로 8x8로 slicing해서
# 8x8 체스보드와 얼마나 다른지를 체크하면 된다

# 그러면 white일 때랑 black일 때를 둘다 비교해야 하나?

board_1 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

board_2 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]


# 서로 다른 요소의 개수를 카운트하는 함수
def count_differences(board1, board2):
    count = 0
    for i in range(len(board1)):  # 행
        for j in range(len(board1[i])):  # 열
            if board1[i][j] != board2[i][j]:  # 두 요소가 다르면 카운트 증가
                count += 1
    return count


records = []
for i in range(M - 7):
    for j in range(N - 7):
        candidate = [row[j : j + 8] for row in large_board[i : i + 8]]
        diff_1 = count_differences(board_1, candidate)
        diff_2 = count_differences(board_2, candidate)
        diff = min(diff_1, diff_2)
        records.append((i, j, diff))

sorted_records = sorted(records, key=lambda x: x[2])

at_least_change = sorted_records[0][2]

print(at_least_change)