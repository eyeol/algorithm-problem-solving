import sys
input = sys.stdin.readline


def solution():
    N = int(input())

    money = 0
    for _ in range(N):
        wid, _ = map(int, input().split())
        if wid == 136:
            money += 1000
        elif wid == 142:
            money += 5000
        elif wid == 148:
            money += 10000
        else:
            money += 50000
    
    print(money)

solution()
