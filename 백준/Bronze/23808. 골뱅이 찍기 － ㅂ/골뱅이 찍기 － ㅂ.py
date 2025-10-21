import sys

input = sys.stdin.readline

def solution():
    N = int(input())

    inter = "@"*N + " "*3*N + "@"*N

    for _ in range(N):
        print(inter)
        print(inter)
    for _ in range(N):
        print("@"*N*5)
    for _ in range(N):
        print(inter)
    for _ in range(N):
        print("@"*N*5)


if __name__ == "__main__":
    solution()
