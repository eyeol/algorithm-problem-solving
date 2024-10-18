h, m = map(int, input().split())

if (diff := m - 45) < 0:
    h -= 1
    m = 60 + diff
else:
    m = diff

h %= 24

print(h, m)
