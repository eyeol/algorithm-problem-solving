import sys

input = sys.stdin.readline

def solution():
    a, b= map(int, input().split())

    if a % b == 0: # 나누어지면
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solution()