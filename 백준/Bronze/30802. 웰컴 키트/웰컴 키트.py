# 티셔츠 종류 6개, 같은 사이즈로 T장씩 주문 가능
# 펜은 한 종류, P자루씩 또는 한자루씩 주문 가능

# N명, 티셔츠 남아도 o, 부족하면 x
# 펜은 정확하게 참가자 수만큼 준비

# 전체 인원 N과
# 사이즈별 인원 S~XXXL이 주어짐
# T와 P가 주어짐

# 구할 것1: 티셔츠를 T장씩 몇번 주문해야함?
# 구할 것2: 펜을 P자루씩 최대 몇 묶음 주문 가능? / 그때 펜을 한자루씩 몇개 주문해야?

N = int(input())

size_list = list(map(int, input().split()))

if sum(size_list) != N:
    raise ValueError("Invalid input: sum of size_list does not match N")

T, P = map(int, input().split())


# size_list의 element ; T로 나눴을 때의 몫 + 1 if 나머지 != 0

num_T = 0
num_P = 0
remain = 0

for size in size_list:
    # 티셔츠 묶음 : 몫을 더하고, 나머지가 0이 아니면 1을 더함
    num_T += size // T + (1 if (size % T != 0) else 0)
    # 펜 묶음 : 몫 + 나머지

num_P += N // P
remain += N % P

print(num_T)
print(num_P, remain)
