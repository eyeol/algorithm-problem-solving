K = int(input())

money_book = []

for i in range(K):
    num = int(input().strip())
    if num == 0:
        money_book.pop(-1)
    else:
        money_book.append(num)

print(sum(money_book))
