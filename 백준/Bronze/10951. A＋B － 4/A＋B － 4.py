import sys

# 입력을 끝까지 처리하기 위해 반복문 사용
for line in sys.stdin:
    # 입력을 공백으로 구분해 두 정수를 A와 B로 나눔
    A, B = map(int, line.split())
    # A와 B의 합을 출력
    print(A + B)
