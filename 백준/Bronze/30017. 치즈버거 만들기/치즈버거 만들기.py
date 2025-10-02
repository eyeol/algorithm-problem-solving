import sys

input = sys.stdin.readline


def solution():
    a, b = map(int, input().split())
    
    if a > b:
        print(b+b+1)
    else:
        print(a+a-1)

if __name__ == "__main__":
    solution()
