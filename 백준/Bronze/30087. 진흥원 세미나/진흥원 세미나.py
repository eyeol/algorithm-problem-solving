import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    for _ in range(N):
        lec = input().strip()
        if lec == "Algorithm":
            print("204")
        elif lec == "DataAnalysis":
            print("207")
        elif lec == "ArtificialIntelligence":
            print("302")
        elif lec == "CyberSecurity":
            print("B101")
        elif lec == "Network":
            print("303")
        elif lec == "Startup":
            print("501")
        else:
            print("105")
    

if __name__ == "__main__":
    solution()
