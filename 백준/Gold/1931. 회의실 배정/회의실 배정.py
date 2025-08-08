import sys
from collections import defaultdict

data = sys.stdin.read().split()
n = int(data[0])

buckets = defaultdict(list)
it = iter(data[1:])
for s, e in zip(it, it):
    buckets[int(s)].append(int(e))

keys = sorted(buckets)           # int 비교
for k in keys:
    buckets[k].sort()            # int 비교

cur_end = -1
cnt = 0
for k in keys:
    for e in buckets[k]:
        if cur_end <= k:         # 겹치지 않으면 회의 선택
            cnt += 1
            cur_end = e          # 종료 시각 갱신
        else:                    # 겹치면 더 빨리 끝나는 회의로 교체
            cur_end = min(cur_end, e)

print(cnt)
