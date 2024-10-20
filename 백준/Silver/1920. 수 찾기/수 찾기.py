N = int(input())

N_list = set(map(int, input().split()))

M = int(input())

M_list = list(map(int, input().split()))

# set 대신에 list를 쓰면 in 연산을 사용할 때 시간 초과 뜬다
# 시간 복잡도 칰쇼
result = []
for num in M_list:
    if num in N_list:
        print(1)
    else:
        print(0)