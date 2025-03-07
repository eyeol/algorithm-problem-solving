# 벌집 중앙 1번방부터 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매김
# 1번방부터 N번방까지 최소 개수의 방을 통해 가는 것

# 규칙성을 찾아야 한다

# 2에서 7까지(6개)는 1 step으로
# 8에서 19까지(12개)는 2step으로
# 20에서 37까지(18개)는 3step으로
# 38에서 61까지(24개)는 4step으로

N = int(input())

# 1 + 6 + 12 + 18 + 24
# 1(base) + 6*1 + 6*2 + 6*3 + 6*4

base = 1
step = 1

while N > base:
    base += 6 * step
    step += 1

print(step)
