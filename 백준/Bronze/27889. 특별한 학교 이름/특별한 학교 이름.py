import sys

input = sys.stdin.readline


def solution():
    letter = input().strip()

    if letter == "NLCS":
        print("North London Collegiate School")
    elif letter == "BHA":
        print("Branksome Hall Asia")
    elif letter == "KIS":
        print("Korea International School")
    elif letter == "SJA":
        print("St. Johnsbury Academy")
    

if __name__ == "__main__":
    solution()
