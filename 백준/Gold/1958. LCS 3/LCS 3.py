import sys
input = sys.stdin.readline

def solution():
    a = input().strip()
    b = input().strip()
    c = input().strip()

    A, B, C = len(a), len(b), len(c)

    prev = [[0] * (C + 1) for _ in range(B + 1)]
    curr = [[0] * (C + 1) for _ in range(B + 1)]

    for i in range(1, A + 1):
        for j in range(1, B + 1):
            for k in range(1, C + 1):
                if a[i-1] == b[j-1] == c[k-1]:
                    curr[j][k] = prev[j-1][k-1] + 1
                else:
                    curr[j][k] = max(
                        prev[j][k],   
                        curr[j-1][k], 
                        curr[j][k-1]  
                    )
        prev, curr = curr, prev 

    print(prev[B][C])

if __name__ == "__main__":
    solution()
