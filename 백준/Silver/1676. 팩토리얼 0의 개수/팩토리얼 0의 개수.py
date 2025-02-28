import sys

input = sys.stdin.readline


def get_factorial(n: int):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def solution():
    N = int(input())
    factorial = str(get_factorial(N))[::-1]

    count = 0
    for number in factorial:
        if number == "0":
            count += 1
        else:
            break

    print(count)


solution()
