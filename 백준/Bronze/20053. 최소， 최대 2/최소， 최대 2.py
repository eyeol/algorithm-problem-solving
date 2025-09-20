import sys

input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
       _ = int(input())
       nums = list(map(int, input().split()))
       print(min(nums), max(nums))



if __name__ == "__main__":
    solution()
