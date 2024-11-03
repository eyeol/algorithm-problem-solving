# 땅 위 달팽이
# 높이 V미터인 나무 막대를 올라갈거임

# 낮에 A미터 올라갈 수 있음
# 밤에 B미터 미끄러짐

# 정상에 올라간 후에는 안미끄러짐

# 나무 막대 모두 올라가려면 며칠 걸리는지 구하자

up, down, height = map(int, input().split())


# 런타임 에러 나오는 방식
# while current < height:
#     day += 1
#     current += up
#     if current >= height:
#         break
#     current -= down

# print(day)

# 수학적으로 구해야한다

# V =< (A-B)*(d-1) + A 면 된다
# 우변 : A(d-1) + A - B(d-1) = A*d - B(d-1)
# d로 묶어보자 ; d(A-B) + B >= V
# d(A-B) >= V-B
# d >= (V-B)/(A-B)

# 나누어떨어지면 그대로 쓰고, 나머지가 있으면 몫 + 1

# V-B
star = height - down

# A-B
moon = up - down

if star % moon == 0:
    day = star // moon
else:
    day = star // moon + 1

print(day)
