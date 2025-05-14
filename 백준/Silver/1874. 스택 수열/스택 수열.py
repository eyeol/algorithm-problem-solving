import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    stack = []
    result = []
    current = 1

    for _ in range(N):
        target = int(input())

        while current <= target:
            stack.append(current)
            result.append("+")
            current += 1

        if stack and stack[-1] == target:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            return

    print('\n'.join(result))

solution()
