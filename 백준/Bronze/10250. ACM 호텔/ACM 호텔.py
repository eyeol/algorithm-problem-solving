T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())

    # 손님이 머무를 층수
    h_index = n % h

    # 딱 맞아떨어지면 0층이 아니라 h층
    if h_index == 0:
        h_index = h
        w_index = n // h
    else:
        w_index = n // h + 1

    print(f"{h_index}{w_index:02}")
