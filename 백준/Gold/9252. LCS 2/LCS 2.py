import sys

input = sys.stdin.readline


def solution():
    X = input().strip()
    Y = input().strip()

    # row
    M = len(X)
    # col
    N = len(Y)

    # row : 0부터 M
    # col : 0부터 N
    choice = [[0 for _ in range(N+1)] for _ in range(M+1)]
    track = [[0 for _ in range(N)] for _ in range(M)]
    # row major
    for i in range(M): # M번 반복하면 됨
        # col
        for j in range(N):
            if X[i] == Y[j]:
                choice[i+1][j+1] = choice[i][j] + 1
                track[i][j] = (-1, -1)
            else: # curr[j] vs prev[j+1]
                if choice[i+1][j] > choice[i][j+1]:
                    choice[i+1][j+1] = choice[i+1][j]
                    track[i][j] = (0, -1)
                else: # prev[j+1] > curr[j]
                    choice[i+1][j+1] = choice[i][j+1]
                    track[i][j] = (-1, 0)
    

    lcs = ""
    
    backtrack_log = []
    cx, cy = M-1, N-1

    while cx >= 0 and cy >= 0:
        nx, ny = track[cx][cy]
        if nx*ny != 0:
            backtrack_log.append(cx)
        cx += nx
        cy += ny
    
    # print(backtrack_log)
    for log in backtrack_log[::-1]:
        lcs += X[log]


    len_lcs = choice[-1][-1]
    if not len_lcs:
        print(len_lcs)
    else:
        print(len_lcs)
        print(lcs)


if __name__ == "__main__":
    solution()
