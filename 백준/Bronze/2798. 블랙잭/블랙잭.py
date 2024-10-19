# 블랙잭

# 카드의 합이 21을 넘지 않는게 조건
# 카드의 합을 최대화하는게 목적

# 새로운 규칙 만들어서 셋이서 게임

# New Version
# 각 카드에는 양의 정수 쓰여있음
# 딜러는 N장의 카드를 모든 숫자가 보이게 세팅
# 딜러가 숫자 M을 크게 외침

# 플레이어는 3장의 카드를 골라서
# 카드 합이 M을 넘지 않으면서 M과 최대한 가까워야함(diff 최소화)

# input : N, M

N, M = map(int, input().split())

num_list = list(map(int, input().split()))

# 방법1 : 모든 3가지 조합을 찾아서 M이랑 가장 가까운 숫자를 print
# 단점 : nC3 모든 경우의 수 찾는게 너무 많음

# 더 좋은 방법 없나
# 다 확인하기 전까지는 뭐가 정답이라고 확신할 수가 없다

# 방법1 채택

sums = []
l = len(num_list)

for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            sums.append(num_list[i] + num_list[j] + num_list[k])

span = []
for num in sums:
    if num <= M:
        span.append(num)

print(max(span))
