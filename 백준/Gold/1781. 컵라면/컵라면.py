import heapq
import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    problems = []
    for _ in range(N):
        deadline, cups = map(int, input().split())
        problems.append((deadline, cups))
        
    # 데드라인 순으로 정렬
    problems.sort(key=lambda x:(x[0]))

    # 데드라인까지 풀 수 있는 문제들
    solved = []
    
    for deadline, cups in problems:
        heapq.heappush(solved, cups)
        if len(solved) > deadline:
            heapq.heappop(solved)
    
    print(sum(solved))


if __name__ == "__main__":
    solution()
