import sys

input = sys.stdin.readline


def solution():
    letter = input().strip()

    if letter == "M":
        print("MatKor")
    elif letter == "W":
        print("WiCys")
    elif letter == "C":
        print("CyKor")
    elif letter == "A":
        print("AlKor")
    else:
        print("$clear")

if __name__ == "__main__":
    solution()
