import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    stack = []
    count = 1

    push_pop = []

    flag = True

    # 숫자가 하나 들어왔을 떄 push pop 표현해야 함
    for _ in range(N):
        number = int(input())

        # count가 number에 도달해야 함
        while count <= number:
            stack.append(count)
            count += 1
            # push
            push_pop.append("+")

        # 마지막 숫자
        if stack:
            pop_num = stack[-1]
            if pop_num < number and count > number:
                flag = False

            while stack and pop_num >= number:

                stack.pop()
                # pop
                push_pop.append("-")

                # pop_num 최신화
                if stack:
                    pop_num = stack[-1]

        else:  # 스택이 빈 경우
            if count > number:
                flag = False

    if flag:
        for operand in push_pop:
            print(operand)
    else:
        print("NO")


solution()
