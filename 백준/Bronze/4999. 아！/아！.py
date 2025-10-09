import sys

input = sys.stdin.readline

def solution():
    ah1 = input().strip()
    ah2 = input().strip()

    if len(ah1) >= len(ah2):
        print("go")
    else:
        print("no")

if __name__ == "__main__":
    solution()