import sys

input = sys.stdin.readline


def add_only_number(word: str):
    return sum(int(ch) for ch in word if ch.isdigit())


def compare(word1: str, word2: str):
    if len(word1) < len(word2):
        return True
    elif len(word1) > len(word2):
        return False
    elif len(word1) == len(word2):
        number1 = add_only_number(word1)
        number2 = add_only_number(word2)

        if number1 != number2:
            return number1 < number2
        else:
            return word1 < word2


def insertion_sort(numbers: list):
    N = len(numbers)
    for i in range(1, N):
        num = numbers[i]
        # 삽입할 위치 탐색용 index
        j = i - 1

        while j >= 0 and not compare(numbers[j], num):
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = num


def solution():
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input().strip())

    # 중복 제거
    words = list(set(words))
    insertion_sort(words)

    for word in words:
        print(word)


solution()
