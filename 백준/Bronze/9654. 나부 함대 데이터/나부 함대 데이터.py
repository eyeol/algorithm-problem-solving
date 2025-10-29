rows = [
    ("N2 Bomber",      "Heavy Fighter",  "Limited",   21),
    ("J-Type 327",     "Light Combat",   "Unlimited",  1),
    ("NX Cruiser",     "Medium Fighter", "Limited",   18),
    ("N1 Starfighter", "Medium Fighter", "Unlimited", 25),
    ("Royal Cruiser",  "Light Combat",   "Limited",    4),
]

# 열 너비: 앞의 두 열 15, 세 번째 11, 마지막 10 (왼쪽 정렬)
print(f'{"SHIP NAME":<15}{"CLASS":<15}{"DEPLOYMENT":<11}{"IN SERVICE":<10}')
for n, c, d, s in rows:
    print(f'{n:<15}{c:<15}{d:<11}{s:<10}')
