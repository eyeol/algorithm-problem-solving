import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    coordinates = [list(map(int, input().split())) for _ in range(N)]

    sorted_coordinates = sorted(coordinates, key=lambda x: (x[1], x[0]))

    for x in sorted_coordinates:
        print(str(x[0]) + " " + str(x[1]))


solution()
