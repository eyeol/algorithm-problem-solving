import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    never_heard = {input().strip() for _ in range(N)}
    never_seen = {input().strip() for _ in range(M)}

    both = sorted(never_heard & never_seen)

    print(len(both))
    print("\n".join(both))


if __name__ == "__main__":
    solution()
