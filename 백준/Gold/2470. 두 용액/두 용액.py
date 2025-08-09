import sys

input = sys.stdin.readline

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
