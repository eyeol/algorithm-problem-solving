# APC

import sys

R = 31
M = 1234567891

input = sys.stdin.readline


def assign_number(alpabet: str):
    return ord(alpabet) - 96


def get_hash(input_str):
    hash_value = 0
    for i, char in enumerate(input_str):
        num = assign_number(char)
        hash_value += num * (R**i)

    return hash_value % M


def solution():
    N = int(input())
    input_str = input().strip()

    hash_value = get_hash(input_str)
    print(hash_value)


solution()
