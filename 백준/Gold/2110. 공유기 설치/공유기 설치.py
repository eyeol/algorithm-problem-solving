import sys

input = sys.stdin.readline

# Given
# 도현이의 집 N개가 수직선 위에 있음
# 각 집의 좌표는 xi로 표현(i는 1부터 N)

# Goal
# 언제 어디서나 와이파이를 즐기기 위해 집에 공유기 C개를 설치하려고 함
# 최대한 많은 곳에서 와이파이 사용하려고 함
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게

# How to solve
# 일단 집들을 일직선으로 놨을 때, 맨 처음 집에 설치하는건 확실
# 최소 거리 D를 이진탐색으로 찾을 것
# 어떻게 찾냐면, safe(D)라는 함수 통해서 되는지 안되는지 체크


def safe(houses: list, d: int, C: int):
    is_safe = True

    # 공유기 설치한 위치 / 맨 왼쪽은 설치 고정
    curr = 0
    count = 1

    # 다음에 설치할 위치 탐색용 인덱스
    next = 1
    while next < len(houses):  # 다음에 설치할 위치가 N이 되면 인덱스 벗어남
        if houses[next] - houses[curr] >= d:
            # 다음 집과 현재 공유기 설치 집의 거리가 d 이상이면 설치
            curr = next
            count += 1
            next += 1
        else:  # 인접 집 거리가 d보다 짧으면 설치 X, 그 다음 집 알아봄
            next += 1

    if count < C:
        is_safe = False

    return is_safe


def solution():
    N, C = map(int, input().split())
    houses = []
    for _ in range(N):
        houses.append(int(input()))
    houses.sort()

    lo, hi = 0, houses[-1] - houses[0]
    ans = 0

    while lo <= hi:
        d = (lo + hi) // 2

        if safe(houses, d, C):
            ans = d
            lo = d + 1
        else:
            hi = d - 1

    print(ans)


if __name__ == "__main__":
    solution()
