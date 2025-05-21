import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    pokedex = [input().strip() for _ in range(N)]

    for _ in range(M):
        pokemon = input().strip()
        if pokemon.isdigit():
            print(pokedex[int(pokemon) - 1])
        else:
            print(pokedex.index(pokemon) + 1)


solution()
