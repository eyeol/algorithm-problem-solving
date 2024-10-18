import sys

for line in sys.stdin:

    edge = list(map(int, line.split()))

    if edge == [0, 0, 0]:
        break

    heru = max(edge)
    edge.remove(heru)

    ausar, auset = edge

    if heru**2 == ausar**2 + auset**2:
        print("right")
    else:
        print("wrong")
