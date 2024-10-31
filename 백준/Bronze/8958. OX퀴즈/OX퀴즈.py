# 와 근데 3중 for문 이게 맞나
T = int(input())

for _ in range(T):
    o_list = list(map(str, input().split("X")))
    sum = 0
    for o_element in o_list:
        for i in range(1, len(o_element) + 1):
            sum += i
    print(sum)
