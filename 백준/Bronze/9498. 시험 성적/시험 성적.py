score = int(input())

if 90 <= score:
    print("A")
elif 80 <= score & score < 90:
    print("B")
elif 70 <= score & score < 80:
    print("C")
elif 60 <= score & score < 70:
    print("D")
else:
    print("F")
