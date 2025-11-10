import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    ans_1 = 0
    ans_2 = 0

    for i in range(1, N+1): # 1부터 N까지
        ans_1 += i
        ans_2 += i**3
    
    print(ans_1)
    print(ans_1**2)
    print(ans_2)

if __name__ == "__main__":
    solution()
