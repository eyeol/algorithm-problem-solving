N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

sorted_points = sorted(points, key=lambda p: (p[0], p[1]))

for point in sorted_points:
    print(f"{point[0]} {point[1]}")
