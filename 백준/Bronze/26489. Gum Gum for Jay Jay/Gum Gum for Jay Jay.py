import sys

input = sys.stdin.readline


def solution():
    ans = 0
    while True:
        if input().strip():
            ans += 1
        else:
            break
    print(ans)

if __name__ == "__main__":
    solution()
