# 소수(Prime Number)가 몇개인지 출력하는게 목표
# 소수는 인수 분해가 안된다, 인수가 1과 자기 자신 뿐
# 근데 1은 소수가 아니다 << 이 부분 주의

import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # 2부터 √n까지만 검사
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


N = int(input())

num_list = list(map(int, input().split()))

num_of_prime = 0

for num in num_list:
    if is_prime(num):
        num_of_prime += 1

print(num_of_prime)
