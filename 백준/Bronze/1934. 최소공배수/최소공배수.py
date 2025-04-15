import sys

input = sys.stdin.readline


# 언제나 A가 B보다 크다
def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


def solution():
    T = int(input())
    for _ in range(T):
        numbers = list(map(int, input().split()))
        A, B = max(numbers), min(numbers)
        LCM = (A * B) // GCD(A, B)
        print(LCM)


solution()
