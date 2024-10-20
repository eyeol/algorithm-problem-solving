import sys

input = sys.stdin.readline

N = int(input())

# stack 동작을 실행시킬 리스트
silver_stack = []

for i in range(N):
    command = input().split()

    if command[0] == "push":
        silver_stack.append(int(command[1]))
    elif command[0] == "pop":
        if len(silver_stack) != 0:
            print(silver_stack.pop(-1))
        else:
            print(-1)

    elif command[0] == "size":
        print(len(silver_stack))
    elif command[0] == "empty":
        if len(silver_stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(silver_stack) != 0:
            print(silver_stack[-1])
        else:
            print(-1)
