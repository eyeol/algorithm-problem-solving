import sys

input = sys.stdin.readline

# Given
# 길이가 N인 정수 배열 A와 B
# A와 B의 요소들을 곱하고 합한걸로 정의된 S

# Goal
# B는 냅두고, A를 재배열해서 S를 최소화하자

# how to solve
# 서로 역방향으로 정렬해서 더하면 되는거 아닌가?


def solution():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort(reverse=True)

    S = 0
    for i in range(N):
        S += A[i] * B[i]

    print(S)


if __name__ == "__main__":
    solution()
