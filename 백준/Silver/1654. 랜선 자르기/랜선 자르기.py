import sys

input = sys.stdin.readline

# Given
# 영식이는 자체적으로 K개의 랜선을 갖고 있음(길이는 제각각)

# Goal
# 같은 길이인, N개의 랜선을 만들어야 함

# How to solve
# 기존 K개의 랜선 중 최소 길이보다 짧거나 같아야 한다
# 어떤 길이를 지정했을 때, 버리는게 생길 수 있음

# 랜선 길이를 d라고 하자
# 만들 수 있는 랜선 갯수는 d에 대한 단조 함수임
# 그래서 d에 대한 파라매트릭 서치라고 볼 수 있음


def ok(wires: list, d: int, N):
    cnt = 0
    for w in wires:
        cnt += w // d
        if cnt >= N:
            return True

    if cnt < N:
        return False


def solution():
    K, N = map(int, input().split())
    wires = [int(input()) for _ in range(K)]

    lo, hi = 1, max(wires)
    ans = 0

    while lo <= hi:
        d = (lo + hi) // 2
        if ok(wires, d, N):
            ans = d
            lo = d + 1
        else:
            hi = d - 1

    print(ans)


if __name__ == "__main__":
    solution()
