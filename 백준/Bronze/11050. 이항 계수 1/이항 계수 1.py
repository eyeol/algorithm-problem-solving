# 이항계수 구하기
# 자연수 N과 정수 K가 주어짐

n, k = map(int, input().split())

result = 1

# 0부터 k-1까지 k번 반복
for i in range(k):
    result *= n - i
    result //= i + 1

print(result)
