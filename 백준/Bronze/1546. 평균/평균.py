# 기말고사 망쳐서 점수 조작하려는 세준
# 자기 점수 중 최댓값 선택 : M
# 모든 점수를 점수/M * 100으로 수정

# 조작된 점수로 새로운 평균 구하는 프로그램 코딩해라

# 첫번째 입력 : 시험본 과목 개수 N < 1000
# 두번째 입력 : 세준 성적

N = int(input())

scores = list(map(int, input().split()))

# 최댓값
M = max(scores)
average = 0

for score in scores:
    average += (score / M) * 100

average /= len(scores)

print(average)
