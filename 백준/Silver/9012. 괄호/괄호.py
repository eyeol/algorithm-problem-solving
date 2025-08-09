import sys

input = sys.stdin.readline

def is_vps(ps: str):
    stack = []
    for ch in ps:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"


def solution():
    T = int(input())

    for _ in range(T):
        ps = input().strip()

        print(is_vps(ps))


if __name__ == "__main__":
    solution()
