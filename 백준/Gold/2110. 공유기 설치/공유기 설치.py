import sys

input = sys.stdin.readline

def safe(houses: list, d: int, C: int) -> bool:
    count = 1
    last = houses[0]
    n = len(houses)
    for i in range(1, n):              
        if houses[i] - last >= d:
            count += 1
            last = houses[i]
            if count >= C:             
                return True
    return False


def solution():
    N, C = map(int, input().split())
    houses = []
    for _ in range(N):
        houses.append(int(input()))
    houses.sort()

  
    lo, hi = 1, houses[-1] - houses[0]  # 최소 간격은 1부터
    ans = 0
    while lo <= hi:
        d = (lo + hi) // 2
        if safe(houses, d, C):
            ans = d
            lo = d + 1
        else:
            hi = d - 1
    print(ans) 


if __name__ == "__main__":
    solution()
