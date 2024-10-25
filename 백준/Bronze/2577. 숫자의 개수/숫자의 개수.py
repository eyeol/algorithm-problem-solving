a = int(input())
b = int(input())
c = int(input())

mul_result = a * b * c

mul_result = list(str(mul_result))

for i in range(0, 10):
    print(mul_result.count(str(i)))
