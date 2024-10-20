# 요세푸스 문제

# N명의 사람이 원을 이루면서 앉음
# 양의 정수 K가 주어짐
# 순서대로 K번째 사람 제거

# N명이 모두 제거될 때까지 해당 과정 반복

# 1 2 3 4 5 6 7  len : 7 / target : 3
# 1 2   4 5 6 7  len : 6 / target : 5  =  2(3-1) + 3   %  6(len)
# 1 2   4 5   7  len : 5 / target : 2  =  4(5-1) + 3   %  5(len)
# 1     4 5   7  len : 4 / target : 4  =  1(2-1) + 3   %  4(len)
# 1     4 5      len : 3 / target : 3  =  3(4-1) + 3   %  3(len)
# 1     4        len : 2 / target : 1  =  2(3-1) + 3   %  2(len)
#       4        len : 1 / target : 1  =

# index : K % N (+K)

# pop한 위치를 기억해둬야 한다 >> index

N, K = map(int, input().split())

round_table = []

# 1부터 N
for i in range(1, N + 1):
    round_table.append(i)


# 제거할 위치 = index % round_table 길이

# index
remove_index = K
# round_table 길이 (N으로 초기화)
table_len = len(round_table)

removed_list = []

# 첫 remove_index
if remove_index != table_len:
    remove_index = remove_index % table_len

while table_len > 0:
    removed = round_table.pop(remove_index - 1)
    removed_list.append(removed)
    # 하나 나가면서 remove_index 재정의

    remove_index = remove_index + K - 1
    table_len -= 1
    if table_len == 0:
        break
    remove_index = remove_index % table_len
    # 나눠떨어지면 table_len만큼 더해줘서 올바른 index 가지도록
    if remove_index == 0:
        remove_index += table_len


result = "<" + ", ".join(map(str, removed_list)) + ">"

print(result)