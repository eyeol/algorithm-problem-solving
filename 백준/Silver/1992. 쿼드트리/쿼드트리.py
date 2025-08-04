import sys
input = sys.stdin.readline

def quad(matrix, r, c, size, out):
    if size == 1:
        out.append(matrix[r][c])
        return

    first = matrix[r][c]
    end_r = r + size
    end_c = c + size
    mat = matrix

    for i in range(r, end_r):
        row = mat[i]
        for j in range(c, end_c):
            if row[j] != first:
                h = size // 2
                out.append('(')
                quad(mat, r,       c,       h, out) 
                quad(mat, r,       c + h,   h, out) 
                quad(mat, r + h,   c,       h, out) 
                quad(mat, r + h,   c + h,   h, out) 
                out.append(')')
                return
    out.append(first)

def solution():
    N = int(input())

    matrix = [input().strip() for _ in range(N)]
    out = []
    quad(matrix, 0, 0, N, out)
    print(''.join(out))

if __name__ == "__main__":
    solution()
