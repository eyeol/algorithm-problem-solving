import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def factorial(N: int):
    if N <= 1:
        return 1
    else:
        return N*factorial(N-1)


def solution():
    N = int(input())
    print(factorial(N))

solution()
