import heapq
import sys

input = sys.stdin.readline

N = int(input())
lecture = []

for _ in range(N):
    lecture.append(list(map(int,input().split())))
lecture.sort(key=lambda x : (x[0],x[1]))

room = [lecture[0][1]]
for i in range(1,N):
    if room[0] <= lecture[i][0]:
        heapq.heappop(room)
    heapq.heappush(room,lecture[i][1])

print(len(room))