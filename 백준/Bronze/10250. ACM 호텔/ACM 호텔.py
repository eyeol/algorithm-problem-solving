T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())

    # 층수
    floor = h if n % h == 0 else n % h

    # 방 번호
    room = (n - 1) // h + 1

    print(f"{floor}{room:02}")
