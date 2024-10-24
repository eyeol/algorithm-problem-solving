N = input()
intN = int(N)
generator = []

# 각 자리수의 합이 최대일 때 M의 범위를 설정
for i in range(max(1, intN - len(N) * 9), intN):  # intN - 자리수 합의 최댓값 부터 시작
    digit_sum = sum(map(int, str(i)))  # i의 각 자리수의 합 계산
    if i + digit_sum == intN:  # i와 각 자리수의 합이 N과 같다면 생성자
        generator.append(i)

if generator:
    print(min(generator))  # 가장 작은 생성자 출력
else:
    print(0)  # 생성자가 없는 경우 0 출력
