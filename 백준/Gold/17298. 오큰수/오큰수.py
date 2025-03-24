import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    A = list(map(int, input().split()))

    result = [-1] * len(A)
    stack = []

    for i in range(len(A)):
        while stack:
            if stack and A[stack[-1]] < A[i]:
                result[stack[-1]] = A[i]
                stack.pop()
            else:
                break

        stack.append(i)

    print(" ".join(map(str, result)))


solution()
