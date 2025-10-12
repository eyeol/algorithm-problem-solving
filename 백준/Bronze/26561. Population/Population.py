import sys

input = sys.stdin.readline

def solution():
    N = int(input())

    for _ in range(N):
        p, t = map(int, input().split())
        dies = t // 7
        born = t // 4

        print(p + born - dies)


if __name__ == "__main__":
    solution()