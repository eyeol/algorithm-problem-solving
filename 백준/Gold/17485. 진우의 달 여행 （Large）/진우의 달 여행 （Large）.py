import sys
input = sys.stdin.readline

INF = 10**15

def solution():
    N, M = map(int, input().split())

    row = list(map(int, input().split()))
    prev = [[row[j]] * 3 for j in range(M)] 

    for _ in range(1, N):
        row = list(map(int, input().split()))
        curr = [[INF, INF, INF] for _ in range(M)]

        last = M - 1
        for j in range(M):
            v = row[j]

            if j > 0:
                t = prev[j - 1]
                curr[j][0] = v + (t[1] if t[1] < t[2] else t[2])

            t = prev[j]
            curr[j][1] = v + (t[0] if t[0] < t[2] else t[2])

            if j < last:
                t = prev[j + 1]
                curr[j][2] = v + (t[0] if t[0] < t[1] else t[1])

        prev = curr

    ans = min(min(cell) for cell in prev)
    print(ans)

if __name__ == "__main__":
    solution()
