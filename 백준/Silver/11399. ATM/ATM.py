# ATM 1대, N명이 줄섰음
# i번째 사람이 돈 뽑는데 P_i분(min) 걸림

# 최솟값은 당연히 적게 걸리는 사람부터 뽑는것

N = int(input())

P_i = list(map(int, input().split()))

P_sorted = sorted(P_i)

time_passed = []
time_took = 0

for time in P_sorted:
    time_took += time
    time_passed.append(time_took)

print(sum(time_passed))
