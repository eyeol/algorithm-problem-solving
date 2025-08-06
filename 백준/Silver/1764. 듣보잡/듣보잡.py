import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    never_heard = {input().strip() for _ in range(N)}

    both = []
    for _ in range(M):
        person = input().strip()
        if person in never_heard:
            both.append(person)

    both.sort()

    print(len(both))
    for person in both:
        print(person)


if __name__ == "__main__":
    solution()
