# 상어 초등학교

import sys
input = sys.stdin.readline

def search_seats(_student):
    max_like = 0
    max_blank = 0
    result = 0
    for r in range(N):
        for c in range(N):
            if shark_class[r][c]:
                continue

            if not result:
                result = (r, c)

            temp_like = 0
            temp_blank = 0
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if shark_class[nr][nc] in _student:
                        temp_like += 1
                    if shark_class[nr][nc] == 0:
                        temp_blank += 1

            if temp_like > max_like:
                max_like = temp_like
                max_blank = temp_blank
                result = (r, c)

            elif temp_like == max_like:
                if temp_blank > max_blank:
                    max_blank = temp_blank
                    result = (r, c)

    return result


def cal_score():
    result = 0
    for r in range(N):
        for c in range(N):
            cnt = 0
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if shark_class[nr][nc] in students_seats[shark_class[r][c]]:
                        cnt += 1
            result += 10**(cnt-1) if cnt > 0 else 0

    return result


N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
drc = [(-1, 0), (0, -1), (1, 0), (0, 1)]

students_seats = [0]*(N**2+1)
shark_class = [[0]*N for _ in range(N)]

for student in students:
    r, c = search_seats(student)
    shark_class[r][c] = student[0]
    students_seats[student[0]] = set(student[1:])

print(cal_score())
