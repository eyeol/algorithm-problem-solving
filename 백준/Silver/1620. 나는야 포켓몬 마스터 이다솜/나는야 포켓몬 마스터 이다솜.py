import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    pokedex_num = [0]
    pokedex_pok = {}

    for i in range(1, N + 1):
        pokemon = input().strip()
        pokedex_num.append(pokemon)
        pokedex_pok[pokemon] = i

    for _ in range(M):
        pokemon = input().strip()
        if pokemon.isdigit():
            print(pokedex_num[int(pokemon)])
        else:
            print(pokedex_pok[pokemon])


solution()
