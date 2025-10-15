import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))  # 정렬 + 중복 제거

path = []
out = []
def dfs(start: int):
    if len(path) == M:
        out.append(" ".join(map(str, path)))
        return
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(i)
        path.pop()

dfs(0)
print("\n".join(out))
