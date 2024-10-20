from collections import Counter

N = int(input())

target = list(map(int, input().split()))

M = int(input())

predict = list(map(int, input().split()))

# 이중 for문을 쓰면 시간초과가 난다
# 그래서 Count 함수를 써야함
target_count = Counter(target)

# Count 함수의 return 형태 기억해두자
for num in predict:
    print(target_count[num], end=" ")