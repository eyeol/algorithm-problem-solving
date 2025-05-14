import sys
from collections import deque

input = sys.stdin.readline


def solution():
    T = int(input())

    for _ in range(T):
        print_log = 0
        length, target = map(int, input().split())

        numbers = list(range(length))  # 0 ~ length-1
        priority = list(map(int, input().split()))

        dq = deque(numbers)
        maximum_priority = max(priority)

        while dq:
            current = dq.popleft()
            if priority[current] != maximum_priority:
                dq.append(current)  # 다시 뒤로
            else:  # 현재가 maximum priority
                priority[current] = 0
                # 출력 순서 로깅
                print_log += 1

                if current == target:
                    break

                # 최대 우선순위 최신화
                maximum_priority = max(priority)

        print(print_log)


solution()
