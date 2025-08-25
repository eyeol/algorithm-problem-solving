import sys

input = sys.stdin.readline

# Given
# 계단 오르기 게임
# 계단 아래 시작점부터 도착점까지 가는 게임
# 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 됨

# 계단 밟는 규칙
# 한번에 한 계단 또는 두 계단씩 오를 수 있음
# 연속된 3개의 계단을 모두 밟으면 안됨(시작점 미포함)
# 마지막 도착 계단은 반드시 밟아야 함

# Goal
# 게임에서 얻을 수 있는 점수의 최대값

# How to solve
# 마지막 계단이 필수니까, 마지막 계단부터 픽스해두고
# recent two(1,2)가 어떤 상태냐에 따라

# 1과 2 둘다 밟았음 -> 3은 무조건 못밟음 확정
# 1만 밟았음 -> 3은 무조건 밟아야 함
# 2만 밟았음 -> 선택 가능(3을 밟을지 4를 밟을지)


def main():
    N = int(input())
    steps = [0]  # 시작점

    for _ in range(N):
        steps.append(int(input()))

    if N == 1:
        print(steps[1])
        return

    if N == 2:
        print(steps[1] + steps[2])
        return

    dp = [0] * (N + 1)
    dp[1] = steps[1]
    dp[2] = steps[1] + steps[2]
    dp[3] = max(steps[1] + steps[3], steps[2] + steps[3])

    for i in range(4, N + 1):
        dp[i] = max(dp[i - 2] + steps[i], dp[i - 3] + steps[i - 1] + steps[i])

    print(dp[N])


if __name__ == "__main__":
    main()
