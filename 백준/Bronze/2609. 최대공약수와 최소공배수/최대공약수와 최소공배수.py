# 2개의 자연수 입력 받아서
# 최대 공약수, 최소 공배수 출력

# 최대 공약수
# 서로 겹치는 약수 중에 최대값

# 최소 공배수
# 서로 겹치는 배수 중에 최소값


# 소인수 분해하는 함수 만들기
def prime_factorize(num):
    prime_factorized = []

    # 약수를 선별
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    # 약수 중에 소인수 아닌 것들 제거
    remove_target = []
    # j : 2 to last
    for j in range(2, len(factors)):
        # 1 to j-1
        for k in range(1, j):
            if factors[j] % factors[k] == 0:
                remove_target.append(j)
                break
    remove_target = sorted(remove_target, reverse=True)

    for index in remove_target:
        factors.pop(index)
    # 이 시점에서 factors에는 소인수만 남는다

    # 입력받은 숫자가 1이 될 때까지 반복
    while num != 1:
        if num % factors[-1] == 0:
            num /= factors[-1]
            prime_factorized.append(factors[-1])
        else:
            factors.pop(-1)

    return prime_factorized


# 집합의 모든 요소 곱해서 반환하는 함수
def product_of_elements(a):
    output = 1
    for number in a:
        output *= number
    return output

a, b = map(int, input().split())

# 소인수 분해
a_composition = prime_factorize(a)
b_composition = prime_factorize(b)


# 서로 겹치는 소인수 구성
prime_composition = set(a_composition).intersection(b_composition)

max_div = 1

# 겹치는 소인수의 지수 정보 구하기
for element in prime_composition:
    # a의 소인수 분해에서 해당 소인수가 몇번 나오는지
    a_count = a_composition.count(element)
    b_count = b_composition.count(element)
    min_exponent = min(a_count, b_count)

    # 겹치는 소인수를 at least 지수 값만큼 곱해줌
    max_div *= element ** (min_exponent)

min_mul = int((a * b) / max_div)

print(max_div)
print(min_mul)


#
#
#
# 잘못된 방법이다
# 약수에서 소인수가 아닌 것들 제거까지는 ok
# 근데 소인수의 지수를 고려하지 못했음
# 24, 32의 경우, 둘다 소인수는 2,3으로 끝이지만
# 최대공약수는 6이 아니라 12(지수까지 고려)
# 추적할거면 소인수의 지수까지 해야한다

# # 인수분해하는 함수 만들기
# def factorziation(num):
#     factors = []

#     # 일단 1~n까지 나눠서 나머지가 0인 애들만 선별해보자
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors.append(i)
#     print(factors)

#     # 얘네는 약수인거지 인수는 아님

#     remove_target = []

#     # 0번째 index는 1인데, 어떤 숫자라도 1로 나누면 나머지 0이라서
#     # 0번째 index는 고려 X
#     # j : 2 to last
#     for j in range(2, len(factors)):
#         # 1 to j-1
#         for k in range(1, j):
#             if factors[j] % factors[k] == 0:
#                 remove_target.append(j)

#     remove_target = list(set(remove_target))
#     remove_target = sorted(remove_target, reverse=True)

#     for index in remove_target:
#         factors.pop(index)

#     # 내가 반환하는건 소인수의 집합
#     return set(factors)


# # 집합의 모든 요소 곱해서 반환하는 함수
# def product_of_elements(set):
#     output = 1
#     for element in set:
#         output *= element
#     return output


# a, b = map(int, input().split())

# a_factors = factorziation(a)
# b_factors = factorziation(b)

# # 이제 인수를 리스트로 받은 상황

# # 최대공약수 = 겹치는 소인수끼리 곱한 숫자

# inter = a_factors.intersection(b_factors)
# max_div = product_of_elements(inter)

# # 최소공배수
# # 일단 a와 b를 곱한다
# # 공배수이긴하지만 그게 최소공배수라는 보장은 x
# # a = (1, - , - , - )
# # b = (1, - , - )

# # 여기서 겹치는게 있으면 그걸로 나눠야 한다
# # 겹치는거 = intersection
# # 어 그러면 a x b 한 다음에 max_div로 나누면 되나

# min_mul = int((a * b) / max_div)

# print(max_div)
# print(min_mul)


#
#
#
#
# 이렇게 풀기 전에 시도한 방법 및 사고 흐름


# 겹치는 약수는 전부 구하면 될듯
# 겹치는 배수는 최소값이니까 구하다가 멈춰야 하는데
# 어떻게 멈추지?

# 겹치는 약수 구해서 list에 저장

# a_div = []
# # 1부터 a까지
# for i in range(1, a + 1):
#     if a % i == 0:
#         a_div.append(i)

# b_div = []
# # 1부터 b까지
# for i in range(1, b + 1):
#     if b % i == 0:
#         b_div.append(i)

# # 두 리스트에서 겹치는 것들 확인
# common_div = set(a_div) & set(b_div)

# max_div = max(common_div)

# # 겹치는 배수는 어떡함
# # 공약수 사용해서 구할 수 있었던거 같은데
# # 인수 분해하는 함수를 만들어볼까

# # 인수 분해해서
# # a = (1, - , -)
# # b = (1, - , -)
