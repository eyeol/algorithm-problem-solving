import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    
    for _ in range(N):
        print("@"*(5*N))
    
    for _ in range(N):
        print("@"*N)

    for _ in range(N):
        print("@"*(5*N))

    for _ in range(N):
        print("@"*N)

    for _ in range(N):
        print("@"*(5*N))

if __name__ == "__main__":
    solution()