N = int(input())


con_1 = N % 4 == 0
con_2 = N % 100 != 0 or N % 400 == 0

if con_1 & con_2:
    print("1")
else:
    print("0")
