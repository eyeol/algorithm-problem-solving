import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    m = [[0]*10 for _ in range(N+1)] # 0은 padding

    # m[n][k] 부터 채우면 됨
    for k in range(10): # 0부터 9
        m[N][k] = 1
    
    for i in range(1, N): # 1부터 N-1
        # N-i 는 N-1부터 1
        for k in range(10):
            m[N-i][k] = sum(m[N-i+1][k:])
    
    result = sum(m[1][0:]) % 10007

    print(result)



if __name__ == "__main__":
    solution()
