import sys

input = sys.stdin.readline


def solution():
    T = int(input().strip())
    for i in range(T):
        a, b = map(int, input().split())
        print(f"Case #{i+1}: {a} + {b} = {a+b}")


solution()
