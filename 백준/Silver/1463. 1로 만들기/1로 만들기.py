from collections import deque

def min_operations_to_one(N):
    # BFS를 위한 큐 생성, (숫자, 연산 횟수) 형태로 저장
    queue = deque([(N, 0)])
    # 이미 방문한 숫자 체크를 위한 집합
    visited = set([N])

    while queue:
        current, operations = queue.popleft()

        # 만약 현재 숫자가 1이면 연산 횟수 반환
        if current == 1:
            return operations

        # 3으로 나눌 수 있으면
        if current % 3 == 0 and current // 3 not in visited:
            queue.append((current // 3, operations + 1))
            visited.add(current // 3)

        # 2로 나눌 수 있으면
        if current % 2 == 0 and current // 2 not in visited:
            queue.append((current // 2, operations + 1))
            visited.add(current // 2)

        # 1을 뺄 수 있으면
        if current - 1 not in visited:
            queue.append((current - 1, operations + 1))
            visited.add(current - 1)

# N을 입력받고 결과 출력
N = int(input())
print(min_operations_to_one(N))
