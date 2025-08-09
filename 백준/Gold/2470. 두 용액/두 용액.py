import sys

input = sys.stdin.readline

# Given
# 산성은 양의 정수로, 염기성은 음의 정수로 나타냄
# 같은 양의 두 용액 혼합한 용액의 특성값 ; 각 용액의 특성값의 합으로 정의됨

# Goal
# 같은 양의 두 용액 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 함

# How to solve
# 언뜻보면 투 포인터인데, 투 포인터로 글로벌 옵티마를 찾을 수 있는건지 검증해야함
# 생각해보니까 양극단에 -100 99가 있어도, 안쪽에 -1, 1 같은 global optima가 있을 수 있음
# 그래서 탐색은 전부 하되, 투 포인터로 탐색하면 됨
# 그러면 투 포인터를 어떤 조건으로 움직일건지
# 어떻게 해야, 불필요한 부분은 체크 안하고, 필요한 부분은 전부 체크하지?
# 더한 결과가 양수인지 음수인지 체크해야할것 같음


def solution():
    N = int(input())
    ph = list(map(int, input().split()))

    ph.sort()

    l, r = 0, N - 1

    global_min = abs(ph[l] + ph[r])
    ans_l, ans_r = 0, N - 1

    while l < r:
        sum = ph[l] + ph[r]
        local_min = abs(sum)
        if local_min < global_min:
            global_min = local_min
            ans_l, ans_r = l, r

        if sum < 0:
            l += 1
        else:  # sum >= 0
            r -= 1

    print(f"{ph[ans_l]} {ph[ans_r]}")


if __name__ == "__main__":
    solution()
