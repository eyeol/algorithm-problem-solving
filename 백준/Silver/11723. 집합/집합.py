import sys

S = set()

input = sys.stdin.readline

M = int(input())

for i in range(M):
    command = input().split()

    if command[0] == "add":
        S.add(int(command[1]))
    elif command[0] == "remove":
        S.discard(int(command[1]))
    elif command[0] == "check":
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if int(command[1]) in S:
            S.discard(int(command[1]))
        else:
            S.add(int(command[1]))
    elif command[0] == "all":
        S = {num for num in range(1, 21)}
    elif command[0] == "empty":
        S = set()
    else:
        raise ValueError("Invalid command")
