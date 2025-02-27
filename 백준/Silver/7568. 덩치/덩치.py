import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    people = []
    ranking = []
    for _ in range(N):
        weight, tall = map(int, input().split())
        people.append((weight, tall))

    for person in people:
        rank = 1
        for person2 in people:
            if person[0] < person2[0] and person[1] < person2[1]:
                rank += 1
        ranking.append(rank)

    for rank in ranking:
        print(rank, end=" ")


solution()
