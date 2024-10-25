a, b, c, d, e = map(int, input().split())
valid = a**2 + b**2 + c**2 + d**2 + e**2

valid %= 10

print(valid)
