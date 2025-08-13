import sys

input = sys.stdin.readline

# 오름차순 정렬
# 앞에서부터 k번째 있는 수


def solution():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()

    print(nums[K - 1])


if __name__ == "__main__":
    solution()
