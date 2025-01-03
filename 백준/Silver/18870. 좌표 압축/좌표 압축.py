import sys

input = sys.stdin.readline

N = int(input())

X = list(map(int, input().split()))

# 중복 제거
Y = list(set(X))
X_sorted = sorted(Y)

compressed = {value: idx for idx, value in enumerate(X_sorted)}

# for i in range(N):
#     compressed[X[i]] = X_sorted.index(X[i])

# for x in X:
#     print(compressed[x], end=" ")
# print()
print(" ".join(str(compressed[x]) for x in X))
