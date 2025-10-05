import heapq
import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    info = []
    for _ in range(N):
        n, s, e = map(int, input().split())
        info.append((n, s, e))
    
    info.sort(key=lambda x:(x[1], x[2], x[0]))
    
    room = []
    room.append(info[0][2]) # 들어가는건 종료 시간
    # 종료 시간보다 그 다음 수업 시작 시간이 뒤면 pop할 수 있음

    for i in range(1, N): # 1부터 N-1
        if room[0] <= info[i][1]:
            heapq.heappop(room)
        heapq.heappush(room, info[i][2])
    
    print(len(room))

if __name__ == "__main__":
    solution()
