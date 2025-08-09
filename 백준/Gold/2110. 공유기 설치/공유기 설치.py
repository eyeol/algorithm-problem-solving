import sys

input = sys.stdin.readline

def safe(houses: list, d: int, C: int):
    curr = 0
    count = 1

    next = 1
    while next < len(houses):  
        if houses[next] - houses[curr] >= d:
            
            curr = next
            count += 1
            next += 1
        else:  
            next += 1
        if count >= C:
            break

    if count < C:
        return False

    return True


def solution():
    N, C = map(int, input().split())
    houses = []
    for _ in range(N):
        houses.append(int(input()))
    houses.sort()

    lo, hi = 0, houses[-1] - houses[0]
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
