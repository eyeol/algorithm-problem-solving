import sys

input = sys.stdin.readline

# Given
# 1개의 회의실, N개의 회의에 대한 회의실 사용표
# 각 회의 i에 대해 시작시간 / 종료시간 주어짐
# 회의 중간에 중단 안됨, 회의 종료와 동시에 다른 회의 시작 가능
# 시작 시간과 종료 시간 같을 수 있음

# 항상 종료 시간이 빠른걸 고르면 된다


def solution():
    N = int(input().strip())

    meetings = []
    for _ in range(N):
        start, end = map(int, input().split())
        meetings.append((start, end))

    # 시작 시간으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))

    curr = 0
    nxt = 1

    # meetings의 첫번쨰 회의는 무조건 select

    # 최초 greedy choice
    curr_end = meetings[curr][1]
    count = 1

    while nxt < N:
        # 현재 미팅 종료시간 vs 다음 미팅 시작 시간 비교
        nxt_start = meetings[nxt][0]
        if curr_end > nxt_start:  # nxt_start가 더 일찍이었다면 그건 이제 안되는 회의
            # curr_end는 갱신 안하고 nxt 다음걸로
            nxt += 1
        else:  # nxt_start가 더 늦다면 회의 선택 가능
            # curr_end 갱신하고 count +1
            curr_end = meetings[nxt][1]
            count += 1
            nxt += 1

    print(count)


if __name__ == "__main__":
    solution()
