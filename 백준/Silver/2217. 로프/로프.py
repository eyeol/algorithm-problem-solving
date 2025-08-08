import sys

input = sys.stdin.readline

# Given
# N개의 로프
# 로프마다 굵기나 길이가 달라서 들 수 있는 물체의 중량이 다를 수 있음
# 여러 로프를 병렬ㄹ로 연결하면, 각각의 로프에 걸리는 중량을 나눌 수 있음
# k개의 로프 사용해 중량 w인 물체 들어올릴 때, 각 로프는 w/k의 하중이 걸림
# 로프들에 대한 정보들 주어짐

# Goal
# 로프들로 들어올릴 수 있는 물체의 최대 중량
# 모든 로프 쓸 필요 X

# how to solve
# 로프가 버틸 수 있는 하중이 너무 작으면, 안쓰는게 낫다
# 안쓰는게 나은지, 그래도 쓰는게 나은지 어떻게 판단?
# 직접 비교말고는 방법이 없어보인다

# how to code
# 직접 비교하는 코드를 짜보자


def solution():
    N = int(input().strip())

    rope_info = []
    for _ in range(N):
        rope_info.append(int(input().strip()))

    rope_num = len(rope_info)
    rope_info.sort()

    maximized_weight = 0
    # 모든 경우를 다 서치해야 한다
    for i in range(rope_num):
        if rope_info[i] * (rope_num - i) > maximized_weight:
            maximized_weight = rope_info[i] * (rope_num - i)

    print(maximized_weight)


if __name__ == "__main__":
    solution()
