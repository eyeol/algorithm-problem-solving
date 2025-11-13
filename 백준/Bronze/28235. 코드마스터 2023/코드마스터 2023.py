import sys

input = sys.stdin.readline


def solution():
    letter = input().strip()

    if letter == "SONGDO":
        print("HIGHSCHOOL")
    elif letter == "CODE":
        print("MASTER")
    elif letter == "2023":
        print("0611")
    elif letter == "ALGORITHM":
        print("CONTEST")
    

if __name__ == "__main__":
    solution()
