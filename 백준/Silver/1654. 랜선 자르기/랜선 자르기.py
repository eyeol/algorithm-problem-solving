import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lan_list = [int(input()) for _ in range(K)]

maximum = sum(lan_list) // N

# sum이 N보다 작거나 같음 : 더 나아갈 수 있음
# sum이 N보다 커짐 : 뒤로 반


def sol():
    result = 0
    start = 1
    end = maximum
    while end >= start:
        target = (start + end) // 2
        # print(start, end, target)
        summation = sum(lan // target for lan in lan_list)
        if summation < N:
            end = target - 1
        elif summation >= N:
            result = target
            start = target + 1

    print(result)


sol()
