# M 이상 N 이하의 소수 구하기
M, N = map(int, input().split())

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


for num in range(M, N + 1):
    if is_prime(num):
        print(num)
