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


def gcd_from_multiple_prime_factors(*factor_lists):
    # zip을 사용해서 각 자리에서 모든 리스트의 최소값을 찾음
    return [min(factors) for factors in zip(*factor_lists)]


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