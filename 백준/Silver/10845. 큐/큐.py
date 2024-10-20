import sys

input = sys.stdin.readline

N = int(input())

# stack 동작을 실행시킬 리스트
silver_que = []

for i in range(N):
    command = input().split()

    if command[0] == "push":
        silver_que.append(int(command[1]))
    elif command[0] == "pop":
        if len(silver_que) != 0:
            print(silver_que.pop(0))
        else:
            print(-1)
    elif command[0] == "size":
        print(len(silver_que))
    elif command[0] == "empty":
        if len(silver_que) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(silver_que) != 0:
            print(silver_que[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(silver_que) != 0:
            print(silver_que[-1])
        else:
            print(-1)
