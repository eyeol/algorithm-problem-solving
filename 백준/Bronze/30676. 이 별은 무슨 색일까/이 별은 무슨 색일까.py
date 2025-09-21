import sys

input = sys.stdin.readline

def solution():
    star = int(input())

    if star < 425:
        print("Violet")
    elif star < 450:
        print("Indigo")
    elif star < 495:
        print("Blue")
    elif star < 570:
        print("Green")
    elif star < 590:
        print("Yellow")
    elif star < 620:
        print("Orange")
    else:
        print("Red")



if __name__ == "__main__":
    solution()