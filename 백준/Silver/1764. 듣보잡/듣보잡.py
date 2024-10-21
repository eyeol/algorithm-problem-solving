# N : 듣도 보도 못한 사람 수
# M : 보도 못한 사람 수

N, M = map(int, input().split())

not_heard_saw = set()
not_saw = set()
for _ in range(N):
    not_heard_saw.add(input())

for _ in range(M):
    not_saw.add(input())

# 사전순 출력을 위한 sorting 잊지말자
not_heard_saw = sorted(not_heard_saw.intersection(not_saw))

print(len(not_heard_saw))
for person in not_heard_saw:
    print(person)
