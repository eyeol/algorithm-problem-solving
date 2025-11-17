import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    site_pwds = {}
    for _ in range(N):
        site, pw = input().split()
        site_pwds[site] = pw
    
    for _ in range(M):
        query = input().strip()
        print(site_pwds[query])
    

if __name__ == "__main__":
    solution()
