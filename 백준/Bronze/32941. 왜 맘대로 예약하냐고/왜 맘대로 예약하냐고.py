import sys

input = sys.stdin.readline

def solution():
    T, X = map(int, input().split())
    
    N = int(input())

    for _ in range(N):
        K = int(input())
        classes = list(map(int, input().split()))
        if X not in classes:
            print("NO")
            return
    
    print("YES")


if __name__ == "__main__":
    solution()