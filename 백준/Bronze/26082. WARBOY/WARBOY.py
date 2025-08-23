a, b, c = map(int, input().split())

# 경쟁사 성능 b
# 경쟁사 가격 a

# 워보이 가격 c
# 워보이 가격대비 성능은 항상 3

# 일반 성능/가격
per_pri = b//a
print(per_pri*3*c)