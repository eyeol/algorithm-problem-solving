import sys
from collections import defaultdict

data = sys.stdin.read().split()
n = int(data[0])

buckets = defaultdict(list)
it = iter(data[1:])
for s, e in zip(it, it):
    buckets[int(s)].append(int(e))

keys = sorted(buckets)           
for k in keys:
    buckets[k].sort()            

cur_end = -1
cnt = 0
for k in keys:
    for e in buckets[k]:
        if cur_end <= k:         
            cnt += 1
            cur_end = e          
        else:                    
            cur_end = min(cur_end, e)

print(cnt)
