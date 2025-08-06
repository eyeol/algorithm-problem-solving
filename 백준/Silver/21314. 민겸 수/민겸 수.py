import sys

input = sys.stdin.readline


def solution():
    s = input().strip()

    mx, mn, m = [], [], 0
    for ch in s:
        if ch == "M":
            m += 1
        else:  # 'K'
            if m > 0:
                mx.append("5" + "0" * m)
                mn.append("1" + "0" * (m - 1) + "5")
                m = 0
            else:
                mx.append("5")
                mn.append("5")

    if m > 0:
        mx.append("1" * m)
        mn.append("1" + "0" * (m - 1))

    print("".join(mx))
    print("".join(mn))


if __name__ == "__main__":
    solution()
