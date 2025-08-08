import sys

input = sys.stdin.readline

# Given
# N 종류의 동전, 종류별로 매우 많이 가지고 있음
# 동전을 적절히 사용(Linear Comb)해서 합을 K로 만들려고 함

# Goal
# 이 때 필요한 동전 개수의 최솟값(계수 합 최소로 만드는)

# how to code
# 동전 가치는 오름차순이라 정렬할 필요 없음
# 가장 가치가 큰 동전을 많이 쓸수록 좋다 ; intuitive한 아이디어
# 가치가 큰 동전부터 mod
# 나머지가 0이 될 떄까지 mod하면 될듯?
# 몫


def solution():
    N, K = map(int, input().split())
    coin_value = []
    for _ in range(N):
        coin_value.append(int(input().strip()))

    i = -1
    count = 0

    # K가 0이 되면 종료되도록
    while K != 0:
        coin = coin_value[i]
        count += K // coin
        K = K % coin
        i -= 1

    print(count)


if __name__ == "__main__":
    solution()
