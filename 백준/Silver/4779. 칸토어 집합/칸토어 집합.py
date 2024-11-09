# 칸토어 집합

# 0과 1사이의 실수 집합
# 각 구간을 3등분하여 가운데를 제외하는 방식

# 그러면 처음엔 3개 (-1) 2개
# 2*3 6개 (-1*2) 4개
# 4*3 12개 (-1*4) 8개

# 제거되는 index
# 전체 list에서의 index 말고
# 나눠진 list 내부에서 index 1, -2로 고정


# 모든 선의 길이가 1이면 멈춘다

# 3^N개면 > N번 반복하고 종료

# 함수가 뭘 받아서 뭘 return하는지 미리 블랙박스로 짜놓고 하는게 좋다


# 3등분 후 가운데를 제거하는 함수
def divide_and_remove(kant: list):
    if len(kant) == 1:
        return kant
    else:
        length = len(kant)
        checkpoint_1 = length // 3
        checkpoint_2 = (length // 3) * 2

        for i in range(checkpoint_1, checkpoint_2):
            kant[i] = " "

        child1 = divide_and_remove(kant[:checkpoint_1])
        child2 = kant[checkpoint_1:checkpoint_2]
        child3 = divide_and_remove(kant[checkpoint_2:])

    return child1 + child2 + child3


# kant를 입력받아서 가운데 제거하고
# child1과 child3를 다시 새로운 kant로 입력해준다
# 각각의 child에서 가운데 제거 하고 각각에서 child를 2개씩 새로


import sys

for line in sys.stdin:
    N = int(line.strip())
    kant = ["-"] * (3**N)

    # 이제 slicing을 해야 하는데
    # 먼저 N만큼 반복문을 써야함

    # 3분할
    # 가운데 제거
    # divide_and_remove()

    # 를 반복
    # 를 하는 함수를 만들어야겠다
    kant = divide_and_remove(kant)

    result = "".join(kant)
    print(result)
