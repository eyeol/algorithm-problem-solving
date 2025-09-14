import sys

input = sys.stdin.readline


def solution():
    K, D, A = map(int, input().split('/'))
    if K+A < D or D == 0:  # 가짜
        print("hasu")
    else:  # 진짜
        print("gosu")



if __name__ == "__main__":
    solution()
