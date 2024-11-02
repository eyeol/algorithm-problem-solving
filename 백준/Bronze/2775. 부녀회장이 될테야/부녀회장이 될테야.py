# 아파트 거주 조건 : a층 b호에 살려면, a-1층의 1호 - b호까지 사람들의 수의 합만큼
# 사람들을 데려와 살아야 한다(이게 뭔소리야)

# 아 그 층에 산 사람은 그만큼 사람들을 데려와 사는게 전제구나
# 그러면 최소 몇명이 살고 있는지를 물어봐야 하는거 아닌가

# 0층의 i호에는 i명이 산다(각층은 1호부터 시작)

# 이 문제를 함수나 클래스 만들어서 풀려면 어떻게 해야할까
# 아니 잠깐 그냥 수학적으로 계산하면 되는거 아닌가

# 0층 1 2 3 4 5 6
# 1층 1 3 6 10 15 21
# 2층 1 4

# 아래 층 불러와서 현재 층의 몇번방에 몇명 사는지 입력하는  함수


def calculate_current_floor_occupants(downstairs):
    current_floor = []
    occupants = 0
    for down_occu in downstairs:
        occupants += down_occu
        current_floor.append(occupants)

    return current_floor


T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    zero_floor = list(range(1, n + 1))
    building = []
    building.append(zero_floor)

    # 1층 to k층
    for i in range(k):
        current_floor = calculate_current_floor_occupants(building[i])
        building.append(current_floor)

    print(sum(building[k - 1]))
