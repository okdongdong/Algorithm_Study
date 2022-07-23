# 노트북의 주인을 찾아서

import sys

input = sys.stdin.readline


def dfs(_student):
    if not check[_student]:

        check[_student] = True

        for laptop in students_laptop_list[_student]:
            if not distributed_laptop[laptop] or dfs(distributed_laptop[laptop]):
                distributed_laptop[laptop] = _student
                return True

    return False


N, M = map(int, input().split())

# 학생 : 노트북 = 1 : 1
students_laptop_list = [[] for _ in range(N+1)]  # 학생별 노트북 후보 리스트
distributed_laptop = [0] * (N+1)  # 노트북별 할당된 학생 리스트

for _ in range(M):
    student, laptop = map(int, input().split())
    students_laptop_list[student].append(laptop)

cnt = 0
for student in range(1, N+1):
    check = [False] * (N+1)

    if dfs(student):
        cnt += 1

print(cnt)
