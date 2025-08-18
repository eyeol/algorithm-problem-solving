import sys
from collections import deque

input = sys.stdin.readline

# Goal
# 큐 구현 후, 입력으로 주어지는 명령을 처리
# 명령은 5가지
# push, pop, size, empty, front, back


def push(deq: deque, x: int):
    deq.append(x)


def pop(deq: deque):
    if not deq:
        print(-1)
    else:
        print(deq.popleft())


def size(deq: deque):
    print(len(deq))


def empty(deq: deque):
    if not deq:
        print(1)
    else:
        print(0)


def front(deq: deque):
    if not deq:
        print(-1)
    else:
        print(deq[0])


def back(deq: deque):
    if not deq:
        print(-1)
    else:
        print(deq[-1])


def solution():
    N = int(input())
    d = deque([])

    for _ in range(N):
        inst = input().split()
        cmd = inst[0]

        if len(inst) == 2:
            x = inst[1]

        if cmd == "push":
            push(d, x)
        elif cmd == "pop":
            pop(d)
        elif cmd == "size":
            size(d)
        elif cmd == "empty":
            empty(d)
        elif cmd == "front":
            front(d)
        elif cmd == "back":
            back(d)
        else:
            print("command error")


if __name__ == "__main__":
    solution()
