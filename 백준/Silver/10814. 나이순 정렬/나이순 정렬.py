N = int(input())

members = []
for i in range(N):
    age, name = input().split()
    # 가입 순서까지 포함한 정보를 tuple로 넣어줌
    members.append((int(age), name, i))

# sorted()가 기본적으로 제공한다는 stable sort가 무엇인지 공부하자
members = sorted(members, key=lambda x: (x[0], x[2]))

for member in members:
    print(f"{member[0]} {member[1]}")
